import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs"
import { join, relative } from "node:path"
import { Plugin } from "@opencode/plugin"
import { UsageRpc, type UsageRow, type UsageSummary, type UsageTokens } from "./rpc.js"

const emptyTokens = (): UsageTokens => ({ input: 0, output: 0, reasoning: 0, cacheRead: 0, cacheWrite: 0, total: 0 })

function addTokens(target: UsageTokens, source: any) {
  target.input += Number(source?.input ?? 0)
  target.output += Number(source?.output ?? 0)
  target.reasoning += Number(source?.reasoning ?? 0)
  target.cacheRead += Number(source?.cache?.read ?? 0)
  target.cacheWrite += Number(source?.cache?.write ?? 0)
  target.total = target.input + target.output + target.reasoning
}

function addRow(rows: Map<string, UsageRow>, key: string, session: any) {
  const row = rows.get(key) ?? { key, cost: 0, sessions: 0, ...emptyTokens() }
  row.cost += Number(session.cost ?? 0)
  row.sessions += 1
  addTokens(row, session.tokens)
  rows.set(key, row)
}

function csvCell(value: unknown) {
  return `"${String(value ?? "").replaceAll('"', '""')}"`
}

export default Plugin.define({
  id: "metro-agents.usage-meter",
  async setup(ctx) {
    const allSessions = async () => {
      const sessions: any[] = []
      let cursor: string | undefined
      do {
        const page: any = await ctx.session.list({ directory: ctx.location.directory, limit: 200, ...(cursor ? { cursor } : {}) })
        sessions.push(...(page.data ?? page))
        cursor = page.cursor?.next ?? undefined
      } while (cursor)
      return sessions
    }

    const summarize = async (sessionID: string): Promise<UsageSummary> => {
      const sessions = await allSessions()
      const byID = new Map(sessions.map((session) => [session.id, session]))
      let root = byID.get(sessionID) ?? await ctx.session.get({ sessionID })
      while (root.parentID && byID.has(root.parentID)) root = byID.get(root.parentID)

      const familyIDs = new Set<string>([root.id])
      let changed = true
      while (changed) {
        changed = false
        for (const session of sessions) {
          if (session.parentID && familyIDs.has(session.parentID) && !familyIDs.has(session.id)) {
            familyIDs.add(session.id)
            changed = true
          }
        }
      }
      const family = sessions.filter((session) => familyIDs.has(session.id))
      if (!family.some((session) => session.id === root.id)) family.unshift(root)

      const totals = emptyTokens()
      const byAgent = new Map<string, UsageRow>()
      const byModel = new Map<string, UsageRow>()
      const byTask = new Map<string, UsageRow>()
      let cost = 0
      const sessionDetails = family.map((session) => {
        const task = session.title?.match(/(?:WEB|API|TRV)-\d{3}/)?.[0] ?? "sin-tarea"
        const agent = session.agent ?? "agente-directo"
        const modelRef = session.model
        const model = modelRef ? `${modelRef.providerID}/${modelRef.id}${modelRef.variant ? `#${modelRef.variant}` : ""}` : "sin-modelo"
        cost += Number(session.cost ?? 0)
        addTokens(totals, session.tokens)
        addRow(byAgent, agent, session)
        addRow(byModel, model, session)
        addRow(byTask, task, session)
        const tokens = emptyTokens()
        addTokens(tokens, session.tokens)
        return {
          id: session.id,
          title: session.title ?? session.id,
          agent,
          model,
          task,
          outcome: session.outcome ?? "unknown",
          durationMs: Math.max(0, Number((session.time?.idle ?? session.time?.updated) ?? 0) - Number(session.time?.created ?? 0)),
          cost: Number(session.cost ?? 0),
          sessions: 1,
          key: session.id,
          ...tokens,
        }
      })

      const todoPath = join(ctx.location.project.directory, "todo.md")
      const todo = existsSync(todoPath) ? readFileSync(todoPath, "utf8") : ""
      const completedTasks = new Set([...todo.matchAll(/^- \[x\] \*\*((?:WEB|API|TRV)-\d{3})\b/gm)].map((match) => match[1]))
      const familyTasks = new Set(sessionDetails.map((session) => session.task).filter((task) => task !== "sin-tarea"))
      const validatedUnits = [...familyTasks].filter((task) => completedTasks.has(task)).length
      const tokenSamples = sessionDetails.map((session) => session.total).filter(Boolean).sort((a, b) => a - b)
      const median = tokenSamples.length ? tokenSamples[Math.floor(tokenSamples.length / 2)] : 0
      const alerts = sessionDetails
        .filter((session) => median > 0 && session.total > median * 2)
        .map((session) => `${session.agent} (${session.task}) consumió más de 2× la mediana de tokens.`)
      return {
        rootSessionID: root.id,
        generatedAt: new Date().toISOString(),
        sessions: family.length,
        cost,
        validatedUnits,
        costPerValidatedUnit: validatedUnits ? cost / validatedUnits : -1,
        tokens: totals,
        byAgent: [...byAgent.values()].sort((a, b) => b.cost - a.cost),
        byModel: [...byModel.values()].sort((a, b) => b.cost - a.cost),
        byTask: [...byTask.values()].sort((a, b) => b.cost - a.cost),
        sessionDetails,
        alerts,
      }
    }

    const registration = await ctx.rpc.register(UsageRpc, {
      summary: async (input) => summarize((input as { sessionID: string }).sessionID),
      exportUsage: async (input) => {
        const { sessionID, format } = input as { sessionID: string; format: "json" | "csv" }
        const summary = await summarize(sessionID)
        const directory = join(ctx.location.project.directory, ".opencode", "usage")
        mkdirSync(directory, { recursive: true })
        const stamp = summary.generatedAt.replaceAll(/[:.]/g, "-")
        const path = join(directory, `usage-${stamp}.${format}`)
        if (format === "json") {
          writeFileSync(path, `${JSON.stringify(summary, null, 2)}\n`)
        } else {
          const columns = ["id", "title", "task", "agent", "model", "outcome", "durationMs", "cost", "input", "output", "reasoning", "cacheRead", "cacheWrite", "total"] as const
          const lines = [columns.join(","), ...summary.sessionDetails.map((session) => columns.map((column) => csvCell(session[column])).join(","))]
          writeFileSync(path, `${lines.join("\n")}\n`)
        }
        return { path: relative(ctx.location.project.directory, path) }
      },
    })

    return () => registration.dispose()
  },
})
