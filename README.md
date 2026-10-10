# Metro Agents

Agent prompts and selectively loaded skills for hierarchical software delivery.

- Runtime configuration: `opencode.jsonc`.
- Delivery entry point: [Hierarchical delivery](.opencode/skills/hierarchical-software-delivery/SKILL.md).
- Technical entry point: [Frontend](.opencode/skills/frontend/frontend-developer/SKILL.md).
- Visual architecture: [UI System Architect](.opencode/skills/frontend/ui-system-architect/SKILL.md).
- Rule/artifact owner locations: `.opencode/skill-ownership.json`.

This repository defines agent responsibilities, handoffs and technical guidance. It does not contain a runnable UI kit or an automated test suite. Token assets are reference data, not evidence of rendered behavior or successful agent execution.

For optional TODO MCP setup, install the TODO extension and configure its server to run `python3 .opencode/tools/run-todo-mcp.py` from the project root. Set `TODO_MCP_SERVER` to the installed extension's `todo-mcp.js` when discovery cannot select exactly one installation; `TODO_MCP_WORKSPACE` overrides the project workspace and `TODO_MCP_NODE` selects Node. Configure the MCP server in the client used for delivery; no Cursor configuration is required by this repository.
