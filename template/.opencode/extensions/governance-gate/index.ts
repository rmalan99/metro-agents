import { existsSync, readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { Plugin } from "@opencode/plugin"
import { GovernanceRpc, type DeliveryStatus } from "./rpc.js"

type Config = {
  strict: boolean
  todoFile: string
  maxConcurrentSubagents: number
  requireTaskBeforeWrite: boolean
  requireAgentLease: boolean
}

type OrchestrationOptions = {
  enabled?: boolean
  directAgent?: string
}

type State = {
  leases: Array<{ agent: string; task: string; scope: string; profile?: string; model?: string; startedAt: string }>
  approvals: Record<string, { brief: string; quote: string; approvedAt: string }>
  taskSessions: Record<string, string>
  executorModels: Record<string, string>
  executorSessions: Record<string, string>
  validations: Record<string, { verdict: "PASS" | "FAIL" | "BLOCKED"; validator: string; report: string; attempts: number; recordedAt: string }>
  recentAgents: Array<{ id: string; task: string; profile: string; model: string; status: string; finishedAt: string }>
}

type MutationAuthorization = {
  allowed: boolean
  reason: "manager-task" | "executor-lease" | "no-active-task" | "no-lease" | "read-only-profile" | "task-not-executing"
  task?: string
}

type RoutingProfile = {
  candidates: string[]
  fallback: string
  requiredCapabilities?: string[]
  preferDifferentFromExecutor?: boolean
}

type RoutingConfig = {
  strict: boolean
  profiles: Record<string, RoutingProfile>
}

const defaults: Config = {
  strict: true,
  todoFile: "todo.md",
  maxConcurrentSubagents: 2,
  requireTaskBeforeWrite: true,
  requireAgentLease: true,
}

const emptyState = (): State => ({ leases: [], approvals: {}, taskSessions: {}, executorModels: {}, executorSessions: {}, validations: {}, recentAgents: [] })

const uiStatus = (status: string) => ({
  preparada: "prepared",
  ejecutando: "implementing",
  verificando: "implemented-awaiting-validation",
  bloqueada: "blocked",
  completada: "completed",
}[status] ?? status)

function readTasks(todoPath: string, state: State): DeliveryStatus["tasks"] {
  if (!existsSync(todoPath)) return []
  const source = readFileSync(todoPath, "utf8")
  const pattern = /^- \[[ x]\] \*\*((?:WEB|API|TRV)-\d{3})\s+[—-]\s+([^*]+)\*\*[\s\S]*?^\s+- Estado:\s*([^\n]+)(?=[\s\S]*?(?:^- \[[ x]\] \*\*(?:WEB|API|TRV)-\d{3}|\s*$))/gm
  return [...source.matchAll(pattern)].map((match) => {
    const validation = state.validations[match[1]]
    let status = uiStatus(match[3].trim())
    const active = state.leases.find((lease) => lease.task === match[1])
    if (active?.profile === "planner") status = "planning"
    else if (active?.profile?.includes("validator")) status = "validating"
    else if (active?.profile?.startsWith("executor")) status = validation?.verdict === "FAIL" ? "correcting" : "implementing"
    else if (validation?.verdict === "PASS" && status !== "completed") status = "validated"
    else if (validation?.verdict === "FAIL" && validation.attempts < 2) status = "correcting"
    else if (state.executorSessions[match[1]] && status === "implementing") status = "implemented-awaiting-validation"
    return {
      id: match[1],
      title: match[2].trim(),
      status,
      attempts: validation?.attempts ?? 0,
      ...(validation ? { verdict: validation.verdict } : {}),
    }
  })
}

function parseModelRef(value: string) {
  const slash = value.indexOf("/")
  if (slash < 1) return undefined
  const providerID = value.slice(0, slash)
  const remainder = value.slice(slash + 1)
  const hash = remainder.lastIndexOf("#")
  return {
    providerID,
    id: hash === -1 ? remainder : remainder.slice(0, hash),
    variant: hash === -1 ? undefined : remainder.slice(hash + 1),
  }
}

function loadJson<T>(path: string, fallback: T): T {
  if (!existsSync(path)) return fallback
  try {
    return { ...fallback, ...JSON.parse(readFileSync(path, "utf8")) }
  } catch {
    return fallback
  }
}

function replaceTaskStatus(todoPath: string, task: string, status: string): boolean {
  if (!existsSync(todoPath)) return false
  const source = readFileSync(todoPath, "utf8")
  const escaped = task.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  const taskBlock = new RegExp(`(^- \\[.\\] \\*\\*${escaped}\\b[\\s\\S]*?)(?=^- \\[.\\] \\*\\*|(?![\\s\\S]))`, "m")
  const match = source.match(taskBlock)
  if (!match) return false
  let updatedBlock = /\n\s+- Estado:/.test(match[1])
    ? match[1].replace(/(\n\s+- Estado:)\s*[^\n]+/, `$1 ${status}`)
    : match[1].replace(/\n/, `\n  - Estado: ${status}\n`)
  updatedBlock = updatedBlock.replace(/^- \[.\]/, status === "completada" ? "- [x]" : "- [ ]")
  writeFileSync(todoPath, source.replace(match[1], updatedBlock))
  return true
}

function readTaskStatus(todoPath: string, task: string): string | undefined {
  if (!existsSync(todoPath)) return undefined
  const source = readFileSync(todoPath, "utf8")
  const escaped = task.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  const match = source.match(new RegExp(`^- \\[[ x]\\] \\*\\*${escaped}\\b[\\s\\S]*?^\\s+- Estado:\\s*([^\\n]+)`, "m"))
  return match?.[1]?.trim()
}

const allowedTransitions: Record<string, string[]> = {
  preparada: ["preparada", "ejecutando", "bloqueada"],
  ejecutando: ["ejecutando", "verificando", "bloqueada"],
  verificando: ["verificando", "ejecutando", "completada", "bloqueada"],
  bloqueada: ["bloqueada", "preparada"],
  completada: ["completada"],
}

export default Plugin.define({
  id: "metro-agents.governance-gate",
  async setup(ctx) {
    const orchestration = (ctx.options.orchestration ?? {}) as OrchestrationOptions
    const orchestrationEnabled = orchestration.enabled !== false
    const directAgent = typeof orchestration.directAgent === "string" && orchestration.directAgent.trim()
      ? orchestration.directAgent.trim()
      : "build"

    const agentRegistration = await ctx.agent.transform((editor) => {
      editor.default(orchestrationEnabled ? "manager" : directAgent)
    })

    if (!orchestrationEnabled) return () => agentRegistration.dispose()

    const root = ctx.location.project.directory
    const configPath = join(root, ".opencode", "governance.json")
    const routingPath = join(root, ".opencode", "model-routing.json")
    const config = loadJson<Config>(configPath, defaults)
    const routing = loadJson<RoutingConfig>(routingPath, { strict: true, profiles: {} })
    config.maxConcurrentSubagents = Math.max(1, Math.min(4, Math.floor(Number(config.maxConcurrentSubagents) || 2)))
    const todoPath = join(root, config.todoFile)
    const stateKey = `governance:${ctx.location.project.id}`

    const storedState = (await ctx.storage.get(stateKey)) as State | undefined
    let leaseState: State = storedState && Array.isArray(storedState.leases)
      ? { ...emptyState(), ...storedState, approvals: storedState.approvals ?? {}, taskSessions: storedState.taskSessions ?? {}, executorModels: storedState.executorModels ?? {}, executorSessions: storedState.executorSessions ?? {}, validations: storedState.validations ?? {}, recentAgents: storedState.recentAgents ?? [] }
      : emptyState()
    const liveLeases = []
    for (const lease of leaseState.leases) {
      try {
        const session: any = await ctx.session.get({ sessionID: lease.agent })
        const terminal = ["succeeded", "failed", "interrupted"].includes(session.outcome)
        const pendingValidator = lease.profile?.includes("validator")
          && !leaseState.validations[lease.task]
          && readTaskStatus(todoPath, lease.task) === "verificando"
        if (!terminal || pendingValidator) {
          liveLeases.push(lease)
          continue
        }
        if (lease.profile?.startsWith("executor") && session.outcome === "succeeded") {
          leaseState.executorModels[lease.task] = lease.model ?? "inherit"
          leaseState.executorSessions[lease.task] = lease.agent
        }
        leaseState.recentAgents.unshift({ id: lease.agent, task: lease.task, profile: lease.profile ?? "subagent", model: lease.model ?? "inherit", status: session.outcome, finishedAt: new Date().toISOString() })
      } catch {
        leaseState.recentAgents.unshift({ id: lease.agent, task: lease.task, profile: lease.profile ?? "subagent", model: lease.model ?? "inherit", status: "recovered-stale-lease", finishedAt: new Date().toISOString() })
      }
    }
    leaseState.leases = liveLeases
    leaseState.recentAgents = leaseState.recentAgents.slice(0, 10)
    if (storedState && liveLeases.length !== storedState.leases.length) await ctx.storage.set(stateKey, leaseState)
    let revision = new Date().toISOString()
    let rpcRegistration: any
    const getState = () => leaseState
    const deliveryStatus = (): DeliveryStatus => {
      const state = getState()
      const tasks = readTasks(todoPath, state)
      const agents = state.leases.map((lease) => ({
        id: lease.agent,
        task: lease.task,
        scope: lease.scope,
        profile: lease.profile ?? "subagent",
        model: lease.model ?? "inherit",
        status: lease.profile === "planner" ? "planning" : lease.profile?.includes("validator") ? "validating" : state.validations[lease.task]?.verdict === "FAIL" ? "correcting" : "implementing",
        startedAt: lease.startedAt,
        ...(lease.profile?.includes("validator") && state.executorSessions[lease.task] ? { validates: state.executorSessions[lease.task] } : {}),
      }))
      const phase = agents[0]?.status ?? tasks.find((task) => task.status !== "completed")?.status ?? (Object.keys(state.approvals).length ? "completed" : "waiting")
      return { phase, revision, activeAgents: agents.length, maxAgents: config.maxConcurrentSubagents, approvalCount: Object.keys(state.approvals).length, tasks, agents, recentAgents: state.recentAgents }
    }
    const setState = async (state: State, reason = "state") => {
      leaseState = state
      revision = new Date().toISOString()
      await ctx.storage.set(stateKey, state)
      await rpcRegistration?.events.emit("updated", { revision, reason })
    }
    const mutationAuthorization = (sessionID: string): MutationAuthorization => {
      const state = getState()
      const lease = state.leases.find((item) => item.agent === sessionID)
      if (lease) {
        if (!lease.profile?.startsWith("executor")) {
          return { allowed: false, reason: "read-only-profile", task: lease.task }
        }
        const status = readTaskStatus(todoPath, lease.task)
        return status === "ejecutando"
          ? { allowed: true, reason: "executor-lease", task: lease.task }
          : { allowed: false, reason: "task-not-executing", task: lease.task }
      }

      const task = Object.entries(state.taskSessions).find(([, owner]) => owner === sessionID)?.[0]
      if (task) {
        const status = readTaskStatus(todoPath, task)
        return status === "ejecutando" || status === "verificando"
          ? { allowed: true, reason: "manager-task", task }
          : { allowed: false, reason: "no-active-task", task }
      }

      return {
        allowed: false,
        reason: state.approvals[sessionID] ? "no-active-task" : "no-lease",
      }
    }

    rpcRegistration = await ctx.rpc.register(GovernanceRpc, {
      status: async () => deliveryStatus(),
      refresh: async () => {
        revision = new Date().toISOString()
        await rpcRegistration.events.emit("updated", { revision, reason: "refresh" })
        return deliveryStatus()
      },
    })

    const listedModels = await ctx.model.list()
    const models = Array.isArray(listedModels)
      ? listedModels
      : Array.isArray((listedModels as any)?.data)
        ? (listedModels as any).data
        : []
    type ModelResolution = {
      ref?: { providerID: string; id: string; variant?: string }
      receipt: string
      unresolved?: boolean
      reasons: string[]
    }
    const resolveModel = (profileName: string, excluded?: string, visited = new Set<string>()): ModelResolution => {
      if (visited.has(profileName)) throw new Error(`Model routing cycle: ${[...visited, profileName].join(" -> ")}`)
      visited.add(profileName)
      const profile = routing.profiles[profileName]
      if (!profile) return { receipt: "error", unresolved: true, reasons: [`profile ${profileName} is not configured`] }
      const reasons: string[] = []
      for (const candidate of profile.candidates ?? []) {
        if (candidate === excluded) {
          reasons.push(`${candidate}: excluded to keep Validator independent`)
          continue
        }
        const ref = parseModelRef(candidate)
        if (!ref) {
          reasons.push(`${candidate}: invalid provider/model reference`)
          continue
        }
        const model = models.find((item: any) => item.providerID === ref.providerID && (item.modelID === ref.id || item.id === ref.id) && item.enabled !== false)
        if (!model) {
          reasons.push(`${candidate}: model is unavailable or disabled`)
          continue
        }
        if (model.status === "deprecated") {
          reasons.push(`${candidate}: model is deprecated`)
          continue
        }
        const variants = Array.isArray(model.variants) ? model.variants : []
        if (ref.variant && !variants.some((variant: any) => (typeof variant === "string" ? variant : variant.id) === ref.variant)) {
          reasons.push(`${candidate}: variant ${ref.variant} is unavailable`)
          continue
        }
        const required = profile.requiredCapabilities ?? []
        if (required.includes("tools") && !model.capabilities?.tools) {
          reasons.push(`${candidate}: tools capability is unavailable`)
          continue
        }
        if (required.includes("vision") && !model.capabilities?.input?.includes("image")) {
          reasons.push(`${candidate}: vision capability is unavailable`)
          continue
        }
        return { ref, receipt: candidate, reasons }
      }
      if (profile.fallback === "inherit") return { receipt: "inherit", reasons }
      if (!profile.fallback || profile.fallback === "error") return { receipt: "error", unresolved: true, reasons }
      const fallback = resolveModel(profile.fallback, excluded, visited)
      return { ...fallback, reasons: [...reasons, ...fallback.reasons] }
    }

    await ctx.agent.transform((editor) => {
      for (const profileName of Object.keys(routing.profiles)) {
        const resolved = resolveModel(profileName)
        if (!resolved.ref || !editor.get(profileName)) continue
        editor.update(profileName, (agent: any) => {
          agent.model = resolved.ref
        })
      }
    })

    await ctx.tool.transform((editor) => {
      editor.namespace({ name: "governance", description: "Register tasks and control subagent concurrency" })

      editor.add({
        name: "approval_record",
        description: "Record the user's explicit approval of one Work Brief before planning or execution",
        input: {
          type: "object",
          properties: { brief: { type: "string" }, userApprovalQuote: { type: "string" } },
          required: ["brief", "userApprovalQuote"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input, context) => {
          const state = getState()
          state.approvals[context.sessionID] = { brief: input.brief, quote: input.userApprovalQuote, approvedAt: new Date().toISOString() }
          await setState(state, "approval-recorded")
          return { content: `Approval recorded for session ${context.sessionID}.` }
        },
      })

      editor.add({
        name: "task_register",
        description: "Register one reviewable task in todo.md before implementation",
        input: {
          type: "object",
          properties: {
            id: { type: "string", pattern: "^(WEB|API|TRV)-[0-9]{3}$" },
            title: { type: "string" },
            scope: { type: "string" },
            acceptance: { type: "string" },
            validation: { type: "string" },
          },
          required: ["id", "title", "scope", "acceptance", "validation"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input, context) => {
          if (!getState().approvals[context.sessionID]) throw new Error("No explicit Work Brief approval is recorded for this session.")
          const state = getState()
          const current = existsSync(todoPath) ? readFileSync(todoPath, "utf8") : "# TODO\n\n"
          if (current.includes(`**${input.id} `)) {
            const owner = state.taskSessions[input.id]
            if (owner && owner !== context.sessionID) throw new Error(`Task ${input.id} is owned by another session.`)
            if (!owner) {
              state.taskSessions[input.id] = context.sessionID
              await setState(state, "task-ownership-migrated")
            }
            return { content: `Task ${input.id} already exists and is owned by this session.` }
          }
          const entry = `- [ ] **${input.id} — ${input.title}**\n  - Estado: preparada\n  - Alcance: ${input.scope}\n  - Criterios de aceptación: ${input.acceptance}\n  - Validación: ${input.validation}\n  - Responsable: Orquestador\n  - Evidencia: pendiente\n\n`
          writeFileSync(todoPath, `${current.trimEnd()}\n\n${entry}`)
          state.taskSessions[input.id] = context.sessionID
          await setState(state, "task-registered")
          revision = new Date().toISOString()
          await rpcRegistration.events.emit("updated", { revision, reason: "task-registered" })
          return { content: `Registered ${input.id} as preparada.` }
        },
      })

      editor.add({
        name: "task_status",
        description: "Move a registered task through preparada, ejecutando, bloqueada, verificando or completada",
        input: {
          type: "object",
          properties: {
            id: { type: "string", pattern: "^(WEB|API|TRV)-[0-9]{3}$" },
            status: { type: "string", enum: ["preparada", "ejecutando", "bloqueada", "verificando", "completada"] },
          },
          required: ["id", "status"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input, context) => {
          const currentStatus = readTaskStatus(todoPath, input.id)
          if (!currentStatus) throw new Error(`Task ${input.id} was not found.`)
          const state = getState()
          const owner = state.taskSessions[input.id]
          if (owner && owner !== context.sessionID) throw new Error(`Task ${input.id} is owned by another session.`)
          if (!owner && state.approvals[context.sessionID]) {
            state.taskSessions[input.id] = context.sessionID
            await setState(state, "task-ownership-migrated")
          }
          if (state.taskSessions[input.id] !== context.sessionID) throw new Error(`Task ${input.id} has no owner for this session.`)
          if (!allowedTransitions[currentStatus]?.includes(input.status)) {
            throw new Error(`Invalid task transition: ${currentStatus} -> ${input.status}.`)
          }
          if (input.status === "completada" && getState().validations[input.id]?.verdict !== "PASS") {
            throw new Error(`Task ${input.id} cannot complete without a recorded Validator PASS.`)
          }
          const changed = replaceTaskStatus(todoPath, input.id, input.status)
          if (changed) {
            revision = new Date().toISOString()
            await rpcRegistration.events.emit("updated", { revision, reason: "task-status" })
          }
          return { content: changed ? `Task ${input.id} moved to ${input.status}.` : `Task ${input.id} was not found.` }
        },
      })

      editor.add({
        name: "agent_launch",
        description: "Resolve a role model, acquire a lease and launch one governed child agent",
        input: {
          type: "object",
          properties: {
            profile: { type: "string", enum: ["planner", "executor-fast", "executor-standard", "executor-deep", "validator", "visual-validator"] },
            task: { type: "string" },
            scope: { type: "string" },
            title: { type: "string" },
            prompt: { type: "string" },
          },
          required: ["profile", "task", "scope", "title", "prompt"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input, context) => {
          const state = getState()
          if (!state.approvals[context.sessionID]) throw new Error("No explicit Work Brief approval is recorded for this session.")
          if (state.leases.length >= config.maxConcurrentSubagents) throw new Error(`Subagent limit reached (${config.maxConcurrentSubagents}).`)
          if (input.profile !== "planner") {
            const status = readTaskStatus(todoPath, input.task)
            if (!status) throw new Error(`Task ${input.task} was not found.`)
            if (state.taskSessions[input.task] !== context.sessionID) throw new Error(`Task ${input.task} is owned by another session.`)
            const validator = input.profile.includes("validator")
            const expectedStatus = validator ? "verificando" : "ejecutando"
            if (status !== expectedStatus) throw new Error(`${input.profile} requires task ${input.task} to be ${expectedStatus}; current status is ${status}.`)
          }
          const route = routing.profiles[input.profile]
          const excluded = route?.preferDifferentFromExecutor ? state.executorModels[input.task] : undefined
          const resolved = resolveModel(input.profile, excluded)
          if (resolved.unresolved) {
            const detail = resolved.reasons.length ? ` ${resolved.reasons.join("; ")}.` : ""
            throw new Error(`No configured model is available for profile ${input.profile}.${detail}`)
          }
          const created = await ctx.session.create({
            parentID: context.sessionID,
            agent: input.profile,
            title: input.title,
            ...(resolved.ref ? { model: resolved.ref } : {}),
          })
          state.leases.push({ agent: created.id, task: input.task, scope: input.scope, profile: input.profile, model: resolved.receipt, startedAt: new Date().toISOString() })
          await setState(state, "agent-launched")
          try {
            await ctx.session.prompt({ sessionID: created.id, text: input.prompt })
          } catch (error) {
            state.leases = state.leases.filter((lease) => lease.agent !== created.id)
            state.recentAgents.unshift({ id: created.id, task: input.task, profile: input.profile, model: resolved.receipt, status: "failed", finishedAt: new Date().toISOString() })
            state.recentAgents = state.recentAgents.slice(0, 10)
            await setState(state, "agent-failed")
            await ctx.session.remove({ sessionID: created.id })
            throw error
          }
          return { content: `Launched ${input.profile} as ${created.id}; model=${resolved.receipt}; active=${state.leases.length}/${config.maxConcurrentSubagents}.` }
        },
      })

      editor.add({
        name: "agent_acquire",
        description: "Reserve one concurrency slot before launching a subagent",
        input: {
          type: "object",
          properties: { agent: { type: "string" }, task: { type: "string" }, scope: { type: "string" } },
          required: ["agent", "task", "scope"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input) => {
          const state = getState()
          if (state.leases.some((lease) => lease.agent === input.agent)) return { content: `Agent ${input.agent} already has a lease.` }
          if (state.leases.length >= config.maxConcurrentSubagents) throw new Error(`Subagent limit reached (${config.maxConcurrentSubagents}).`)
          state.leases.push({ ...input, startedAt: new Date().toISOString() })
          await setState(state, "lease-acquired")
          return { content: `Lease acquired for ${input.agent}. Active: ${state.leases.length}/${config.maxConcurrentSubagents}.` }
        },
      })

      editor.add({
        name: "agent_release",
        description: "Release a subagent concurrency slot after it finishes or is interrupted",
        input: {
          type: "object",
          properties: { agent: { type: "string" } },
          required: ["agent"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input) => {
          const state = getState()
          const released = state.leases.find((lease) => lease.agent === input.agent)
          if (released?.profile?.startsWith("executor") && released.model) {
            state.executorModels[released.task] = released.model
            state.executorSessions[released.task] = released.agent
          }
          if (released) {
            state.recentAgents.unshift({ id: released.agent, task: released.task, profile: released.profile ?? "subagent", model: released.model ?? "inherit", status: "finished", finishedAt: new Date().toISOString() })
            state.recentAgents = state.recentAgents.slice(0, 10)
          }
          state.leases = state.leases.filter((lease) => lease.agent !== input.agent)
          await setState(state, "agent-released")
          return { content: `Lease released for ${input.agent}. Active: ${state.leases.length}/${config.maxConcurrentSubagents}.` }
        },
      })

      editor.add({
        name: "validation_record",
        description: "Record an independent Validator verdict; a PASS is required before task completion",
        input: {
          type: "object",
          properties: {
            task: { type: "string" },
            validatorSession: { type: "string" },
            verdict: { type: "string", enum: ["PASS", "FAIL", "BLOCKED"] },
            report: { type: "string" },
          },
          required: ["task", "validatorSession", "verdict", "report"],
          additionalProperties: false,
        },
        options: { codemode: true },
        execute: async (input) => {
          const state = getState()
          const lease = state.leases.find((item) => item.agent === input.validatorSession && item.task === input.task)
          if (!lease?.profile?.includes("validator")) throw new Error("Verdict must come from an active Validator lease for the same task.")
          const previousAttempts = state.validations[input.task]?.attempts ?? 0
          const attempts = previousAttempts + (input.verdict === "BLOCKED" ? 0 : 1)
          state.validations[input.task] = { verdict: input.verdict, validator: input.validatorSession, report: input.report, attempts, recordedAt: new Date().toISOString() }
          const exhausted = input.verdict === "FAIL" && attempts >= 2
          if (exhausted) replaceTaskStatus(todoPath, input.task, "bloqueada")
          await setState(state, exhausted ? "validation-blocked" : `validation-${input.verdict.toLowerCase()}`)
          const attemptReceipt = input.verdict === "BLOCKED"
            ? `validation attempt not consumed; ${attempts} completed`
            : `validation attempt ${attempts}`
          return { content: `Recorded ${input.verdict} for ${input.task}; ${attemptReceipt}.${exhausted ? " Task blocked for user escalation." : ""}` }
        },
      })
    })

    await ctx.session.hook("context", async (event) => {
      if (!config.strict) return
      const state = getState()
      const authorization = mutationAuthorization(event.sessionID)
      const mutationAllowed = authorization.reason !== "read-only-profile"
        && (!config.requireTaskBeforeWrite || authorization.allowed)

      for (const name of Object.keys(event.tools)) {
        const normalized = name.toLowerCase()
        const sessionLease = state.leases.find((lease) => lease.agent === event.sessionID)
        const leaseRequired = config.requireAgentLease && !state.approvals[event.sessionID] && !sessionLease
        if ((!mutationAllowed || leaseRequired) && /(write|edit|patch|bash|shell)/.test(normalized) && !normalized.includes("governance")) {
          delete event.tools[name]
        }
      }

      event.system.push({
        type: "text",
        text: `Governance gate: todo=${config.todoFile}; mutationAllowed=${mutationAllowed}; authorization=${authorization.reason}; task=${authorization.task ?? "none"}; activeSubagents=${state.leases.length}/${config.maxConcurrentSubagents}. Managers own task state; only an Executor lease authorizes delegated code mutation while its task is ejecutando. Planner and Validator leases are read-only. Release leases on completion or interruption.`,
      })
    })

    return async () => {
      await rpcRegistration?.dispose()
      await agentRegistration.dispose()
    }
  },
})
