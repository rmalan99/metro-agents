import { Rpc } from "@opencode/plugin/rpc"

const statusSchema = {
  type: "object",
  properties: {
    phase: { type: "string" },
    revision: { type: "string" },
    activeAgents: { type: "integer" },
    maxAgents: { type: "integer" },
    approvalCount: { type: "integer" },
    tasks: { type: "array", items: { type: "object", additionalProperties: true } },
    agents: { type: "array", items: { type: "object", additionalProperties: true } },
    recentAgents: { type: "array", items: { type: "object", additionalProperties: true } },
  },
  required: ["phase", "revision", "activeAgents", "maxAgents", "approvalCount", "tasks", "agents", "recentAgents"],
  additionalProperties: false,
} as const

export const GovernanceRpc = Rpc.define({
  id: "metro-governance",
  methods: {
    status: { input: { type: "object", additionalProperties: false }, output: statusSchema },
    refresh: { input: { type: "object", additionalProperties: false }, output: statusSchema },
  },
  events: {
    updated: {
      schema: {
        type: "object",
        properties: { revision: { type: "string" }, reason: { type: "string" } },
        required: ["revision", "reason"],
        additionalProperties: false,
      },
    },
  },
})

export type DeliveryStatus = {
  phase: string
  revision: string
  activeAgents: number
  maxAgents: number
  approvalCount: number
  tasks: Array<{ id: string; title: string; status: string; verdict?: string; attempts: number }>
  agents: Array<{ id: string; task: string; scope: string; profile: string; model: string; status: string; startedAt: string; validates?: string }>
  recentAgents: Array<{ id: string; task: string; profile: string; model: string; status: string; finishedAt: string }>
}
