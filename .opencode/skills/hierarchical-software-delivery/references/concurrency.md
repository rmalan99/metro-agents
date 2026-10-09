# Delivery concurrency

Orchestrator and Leads read this for allocation/dispatch; Juniors receive their assigned ownership through Task quality.

- Maximum two active Junior invocations per Lead and four across delivery. These are instruction limits, not a runtime scheduler.
- Orchestrator reserves junior_slot_budget of 1 or 2 per unfinished dispatched Work Order; total reservations must not exceed four. An absent budget requires sequential one-slot execution and a global reservation, not an uncounted worker.
- Count an invocation as active until completion or confirmed cancellation. Timeout does not release it; replacements cannot overlap unresolved workers.
- Use concurrent calls only when the runtime supports them. Otherwise run sequentially and disclose the limitation.
- Task write scopes must be disjoint, reads cannot overlap another worker's changing artifacts, and exclusive resources cannot be shared. Declare paths, ports, databases, fixtures and outputs in Task quality.
- Agree shared contracts before dispatch. Resolve cross-team ownership conflicts through the Orchestrator; uncertain independence means sequential execution.
- Launch dependent tasks only after prerequisite acceptance. Release/reassign budgets when the corresponding work and active workers finish.
