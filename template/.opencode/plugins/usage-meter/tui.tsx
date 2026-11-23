import { Plugin } from "@opencode/plugin/tui"
import { For, Show, createSignal, onMount } from "solid-js"
import { UsageRpc, type UsageSummary } from "./rpc.js"

const formatTokens = (value: number) => value >= 1_000_000 ? `${(value / 1_000_000).toFixed(2)}M` : value >= 1_000 ? `${(value / 1_000).toFixed(1)}K` : String(value)
const formatCost = (value: number) => `$${value.toFixed(value < 0.01 ? 4 : 2)}`

export default Plugin.define({
  id: "metro-agents.usage-tui",
  setup(context) {
    const rpc = context.client.rpc(UsageRpc)

    const UsagePanel = (props: { panel: { sessionID?: string; close: () => void; toggleFullscreen: () => void } }) => {
      const [summary, setSummary] = createSignal<UsageSummary>()
      const [error, setError] = createSignal("")

      const load = async () => {
        if (!props.panel.sessionID) return
        try {
          setError("")
          setSummary(await rpc.summary({ sessionID: props.panel.sessionID }) as UsageSummary)
        } catch (cause) {
          setError(cause instanceof Error ? cause.message : "No se pudo medir la sesión.")
        }
      }

      const exportUsage = async (format: "json" | "csv") => {
        if (!props.panel.sessionID) return
        const result = await rpc.exportUsage({ sessionID: props.panel.sessionID, format }) as { path: string }
        context.ui.toast.show({ title: "Usage Meter", message: `Exportado: ${result.path}`, variant: "success" })
      }

      onMount(() => void load())
      context.keymap.layer(() => ({
        commands: [
          { id: "metro.usage.close", bind: "escape", run: props.panel.close },
          { id: "metro.usage.fullscreen", bind: "f", run: props.panel.toggleFullscreen },
          { id: "metro.usage.refresh-panel", bind: "r", run: load },
          { id: "metro.usage.export-json-panel", bind: "j", run: () => exportUsage("json") },
          { id: "metro.usage.export-csv-panel", bind: "c", run: () => exportUsage("csv") },
        ],
      }))

      return (
        <box flexDirection="column" padding={1}>
          <text fg={context.theme.text.base}>Consumo local</text>
          <Show when={error()}><text fg={context.theme.text.danger}>{error()}</text></Show>
          <Show when={summary()} fallback={<text fg={context.theme.text.muted}>Calculando consumo real…</text>}>
            {(data) => (
              <box flexDirection="column">
                <text fg={context.theme.text.base}>Total {formatCost(data().cost)} · {formatTokens(data().tokens.total)} tokens · {data().sessions} sesiones</text>
                <text fg={context.theme.text.muted}>Entrada {formatTokens(data().tokens.input)} · salida {formatTokens(data().tokens.output)} · razonamiento {formatTokens(data().tokens.reasoning)}</text>
                <text fg={context.theme.text.muted}>Caché leída {formatTokens(data().tokens.cacheRead)} · escrita {formatTokens(data().tokens.cacheWrite)}</text>
                <text fg={context.theme.text.muted}>Unidades validadas {data().validatedUnits} · coste/unidad {data().costPerValidatedUnit < 0 ? "sin datos" : formatCost(data().costPerValidatedUnit)}</text>

                <text fg={context.theme.text.base}>Por agente</text>
                <For each={data().byAgent}>{(row) => <text fg={context.theme.text.muted}>{row.key} · {formatCost(row.cost)} · {formatTokens(row.total)}</text>}</For>

                <text fg={context.theme.text.base}>Por modelo</text>
                <For each={data().byModel}>{(row) => <text fg={context.theme.text.muted}>{row.key} · {formatCost(row.cost)} · {formatTokens(row.total)}</text>}</For>

                <text fg={context.theme.text.base}>Por tarea</text>
                <For each={data().byTask}>{(row) => <text fg={context.theme.text.muted}>{row.key} · {formatCost(row.cost)} · {formatTokens(row.total)}</text>}</For>

                <Show when={data().alerts.length > 0}>
                  <text fg={context.theme.text.base}>Alertas</text>
                  <For each={data().alerts}>{(alert) => <text fg={context.theme.text.warning}>⚠ {alert}</text>}</For>
                </Show>
              </box>
            )}
          </Show>
          <text fg={context.theme.text.muted}>r actualizar · j JSON · c CSV · f pantalla completa · esc cerrar</text>
        </box>
      )
    }

    const panelSlot = context.ui.slot({
      append: "session.panel",
      render: (panel) => <Show when={panel.name === "metro.usage"}><UsagePanel panel={panel} /></Show>,
    })

    context.keymap.layer(() => ({
      mode: "global",
      commands: [
        {
          id: "metro.usage",
          title: "Mostrar consumo local",
          group: "Metro Agents",
          palette: true,
          slash: { name: "usage" },
          run: () => context.ui.panel.open("metro.usage"),
        },
      ],
    }))

    return panelSlot
  },
})
