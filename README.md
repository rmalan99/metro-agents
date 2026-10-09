# Metro Agents

Agent prompts and selectively loaded skills for hierarchical software delivery.

- Runtime configuration: `opencode.jsonc`.
- Delivery entry point: [Hierarchical delivery](.opencode/skills/hierarchical-software-delivery/SKILL.md).
- Technical entry point: [Frontend](.opencode/skills/frontend/frontend-developer/SKILL.md).
- Rule/artifact owner locations: `.opencode/skill-ownership.json`.
- Local checks and runtime limitations: [Validation](docs/validation.md).
- Optional task-provider setup: [TODO MCP](docs/todo-mcp.md).

Local validation requires Python 3 and uses the standard library:

```sh
python3 .opencode/tools/validate-repository.py
python3 -m unittest discover -s tests -v
```

CI runs the same checks. No agent/model execution or external MCP service is implied by a successful static check.
