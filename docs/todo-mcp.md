# Portable TODO MCP setup

The repository policy is in [AGENTS](../AGENTS.md); tool arguments belong to the [TODO catalog](../.agents/skills/todo-tracker/SKILL.md).

The project Cursor configuration invokes `.opencode/tools/run-todo-mcp.py` using Python 3 from the repository root. If a client starts elsewhere, resolve this bootstrap path through that client's supported workspace-path mechanism. Do not reintroduce a contributor's home path into committed configuration.

Prerequisites: Python 3, Node and an installed TODO extension providing `bin/todo-mcp.js`. The bootstrap discovers a single installation in standard Cursor/VS Code extension directories. With no installation or multiple candidates, set `TODO_MCP_SERVER` to the actual script path through your environment/client settings.

Optional environment variables:
- `TODO_MCP_WORKSPACE`: workspace to manage; defaults to this repository, independent of process working directory.
- `TODO_MCP_NODE`: Node executable/name; defaults to `node`.

Paths are passed as argv, so spaces require no shell construction. The bootstrap never installs an extension, creates tasks or edits `.todo`.

For OpenCode, configure a local MCP server whose command is `python3 .opencode/tools/run-todo-mcp.py` using the installed runtime's supported local-server configuration. This repository does not enable an unavailable server implicitly. Verify `todo_get_tasks` is exposed before using task operations; report a missing provider instead of editing the task file.
