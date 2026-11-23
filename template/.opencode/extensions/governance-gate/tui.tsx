import { Plugin } from "@opencode/plugin/tui"
import { For, Show, createSignal } from "solid-js"
import { GovernanceRpc, type DeliveryStatus } from "./rpc.js"

const EMPTY: DeliveryStatus = {
  phase: "waiting",
  revision: "",
  activeAgents: 0,
  maxAgents: 2,
  approvalCount: 0,
  tasks: [],
  agents: [],
  recentAgents: [],
}

const labels: Record<string, string> = {
  waiting: "En espera",
  planning: "Planificando",
  prepared: "Preparada",
  implementing: "Implementando",
  "implemented-awaiting-validation": "Implementada · espera validación",
  validating: "Validando",
  validated: "Validada",
  correcting: "Corrigiendo",
  blocked: "Bloqueada",
  completed: "Completada",
}

const label = (value: string) => labels[value] ?? value

export default Plugin.define({
  id: "metro-agents.governance-tui",
  async setup(context) {
    const orchestration = (context.options.orchestration ?? {}) as { enabled?: boolean }
    if (orchestration.enabled === false) return

    const [status, setStatus] = createSignal<DeliveryStatus>(EMPTY)
    const rpc = context.client.rpc(GovernanceRpc)

    const load = async (refresh = false) => {
      try {
        const next = await (refresh ? rpc.refresh({}) : rpc.status({}))
        setStatus(next as DeliveryStatus)
      } catch {
        setStatus((current) => ({ ...current, phase: "waiting" }))
      }
    }

    await load()
    const stopEvents = rpc.events.on("updated", (event) => {
      void load()
      const reason = (event.data as { reason?: string }).reason
      if (reason === "validation-pass") context.ui.toast.show({ title: "Metro Agents", message: "Unidad validada", variant: "success" })
      if (reason === "validation-fail") context.ui.toast.show({ title: "Metro Agents", message: "Validación fallida; se requiere corrección", variant: "warning" })
      if (reason === "validation-blocked") context.ui.toast.show({ title: "Metro Agents", message: "Unidad bloqueada", variant: "error" })
    })

    const Sidebar = () => (
      <box flexDirection="column" paddingTop={1}>
        <text fg={context.theme.text.muted}>ENTREGA · agentes {status().activeAgents}/{status().maxAgents}</text>
        <text fg={context.theme.text.base}>{label(status().phase)}</text>
        <For each={status().agents}>
          {(agent) => (
            <box flexDirection="column" paddingTop={1}>
              <text fg={context.theme.text.base}>● {agent.task} · {label(agent.status)}</text>
              <text fg={context.theme.text.muted}>{agent.profile} · {agent.model}</text>
            </box>
          )}
        </For>
        <Show when={status().agents.length === 0 && status().tasks[0]}>
          {(task) => <text fg={context.theme.text.muted}>{task().id} · {label(task().status)}</text>}
        </Show>
      </box>
    )

    const DeliveryPanel = (props: { panel: { close: () => void; toggleFullscreen: () => void } }) => {
      context.keymap.layer(() => ({
        commands: [
          { id: "metro.delivery.close", bind: "escape", run: props.panel.close },
          { id: "metro.delivery.fullscreen", bind: "f", run: props.panel.toggleFullscreen },
          { id: "metro.delivery.refresh-panel", bind: "r", run: () => load(true) },
        ],
      }))
      return (
        <box flexDirection="column" padding={1}>
          <text fg={context.theme.text.base}>Entrega · {label(status().phase)}</text>
          <text fg={context.theme.text.muted}>Agentes activos: {status().activeAgents}/{status().maxAgents}</text>
          <For each={status().agents}>
            {(agent) => (
              <box flexDirection="column" paddingTop={1}>
                <text fg={context.theme.text.base}>{agent.profile} · {agent.task}</text>
                <text fg={context.theme.text.muted}>{label(agent.status)} · {agent.model}</text>
                <text fg={context.theme.text.muted}>Lease: {agent.scope}</text>
                <Show when={agent.validates}><text fg={context.theme.text.muted}>Valida: {agent.validates}</text></Show>
              </box>
            )}
          </For>
          <text fg={context.theme.text.base}>Unidades</text>
          <For each={status().tasks}>
            {(task) => <text fg={context.theme.text.muted}>{task.id} · {label(task.status)}{task.verdict ? ` · ${task.verdict}` : ""}</text>}
          </For>
          <Show when={status().recentAgents.length > 0}>
            <text fg={context.theme.text.base}>Actividad reciente</text>
            <For each={status().recentAgents.slice(0, 5)}>
              {(agent) => <text fg={context.theme.text.muted}>{agent.profile} · {agent.task} · {agent.status}</text>}
            </For>
          </Show>
          <text fg={context.theme.text.muted}>r actualizar · f pantalla completa · esc cerrar</text>
        </box>
      )
    }

    const disposers = [
      context.ui.slot({ append: "sidebar.content", render: () => <Sidebar /> }),
      context.ui.slot({ append: "home.footer.status", render: () => <text fg={context.theme.text.muted}>ENTREGA {label(status().phase)} · {status().activeAgents}/{status().maxAgents}</text> }),
      context.ui.slot({
        append: "session.panel",
        render: (panel) => <Show when={panel.name === "metro.delivery"}><DeliveryPanel panel={panel} /></Show>,
      }),
    ]

    context.keymap.layer(() => ({
      mode: "global",
      commands: [
        {
          id: "metro.delivery",
          title: "Mostrar estado de entrega",
          group: "Metro Agents",
          palette: true,
          slash: { name: "delivery" },
          run: () => context.ui.panel.open("metro.delivery"),
        },
        {
          id: "metro.delivery.refresh",
          title: "Actualizar estado de entrega",
          group: "Metro Agents",
          palette: true,
          slash: { name: "delivery-refresh" },
          run: async () => {
            await load(true)
            context.ui.toast.show({ title: "Metro Agents", message: "Estado actualizado", variant: "success" })
          },
        },
      ],
    }))

    return () => {
      stopEvents()
      for (const dispose of disposers) dispose()
    }
  },
})
