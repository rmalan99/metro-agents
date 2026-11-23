import { Rpc } from "@opencode/plugin/rpc"

const requestSchema = {
  type: "object",
  properties: { sessionID: { type: "string" } },
  required: ["sessionID"],
  additionalProperties: false,
} as const

const tokenProperties = {
  input: { type: "number" },
  output: { type: "number" },
  reasoning: { type: "number" },
  cacheRead: { type: "number" },
  cacheWrite: { type: "number" },
  total: { type: "number" },
} as const

const rowSchema = {
  type: "object",
  properties: { key: { type: "string" }, cost: { type: "number" }, sessions: { type: "integer" }, ...tokenProperties },
  required: ["key", "cost", "sessions", "input", "output", "reasoning", "cacheRead", "cacheWrite", "total"],
  additionalProperties: false,
} as const

const sessionSchema = {
  type: "object",
  properties: {
    ...rowSchema.properties,
    id: { type: "string" }, title: { type: "string" }, agent: { type: "string" }, model: { type: "string" },
    task: { type: "string" }, durationMs: { type: "number" }, outcome: { type: "string" },
  },
  required: [...rowSchema.required, "id", "title", "agent", "model", "task", "durationMs", "outcome"],
  additionalProperties: false,
} as const

const summarySchema = {
  type: "object",
  properties: {
    rootSessionID: { type: "string" },
    generatedAt: { type: "string" },
    sessions: { type: "integer" },
    cost: { type: "number" },
    validatedUnits: { type: "integer" },
    costPerValidatedUnit: { type: "number" },
    tokens: { type: "object", properties: tokenProperties, required: ["input", "output", "reasoning", "cacheRead", "cacheWrite", "total"], additionalProperties: false },
    byAgent: { type: "array", items: rowSchema },
    byModel: { type: "array", items: rowSchema },
    byTask: { type: "array", items: rowSchema },
    sessionDetails: { type: "array", items: sessionSchema },
    alerts: { type: "array", items: { type: "string" } },
  },
  required: ["rootSessionID", "generatedAt", "sessions", "cost", "validatedUnits", "costPerValidatedUnit", "tokens", "byAgent", "byModel", "byTask", "sessionDetails", "alerts"],
  additionalProperties: false,
} as const

export const UsageRpc = Rpc.define({
  id: "metro-usage",
  methods: {
    summary: { input: requestSchema, output: summarySchema },
    exportUsage: {
      input: {
        type: "object",
        properties: { sessionID: { type: "string" }, format: { type: "string", enum: ["json", "csv"] } },
        required: ["sessionID", "format"],
        additionalProperties: false,
      },
      output: {
        type: "object",
        properties: { path: { type: "string" } },
        required: ["path"],
        additionalProperties: false,
      },
    },
  },
  events: {},
})

export type UsageTokens = { input: number; output: number; reasoning: number; cacheRead: number; cacheWrite: number; total: number }
export type UsageRow = UsageTokens & { key: string; cost: number; sessions: number }
export type UsageSummary = {
  rootSessionID: string
  generatedAt: string
  sessions: number
  cost: number
  validatedUnits: number
  costPerValidatedUnit: number
  tokens: UsageTokens
  byAgent: UsageRow[]
  byModel: UsageRow[]
  byTask: UsageRow[]
  sessionDetails: Array<UsageRow & { id: string; title: string; agent: string; model: string; task: string; durationMs: number; outcome: string }>
  alerts: string[]
}
