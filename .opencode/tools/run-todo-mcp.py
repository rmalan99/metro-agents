"""Resolve a local TODO extension server without personal paths or shell interpolation."""
from pathlib import Path
import os
import shutil
import sys


def resolve_command(env, project_root, user_home):
    workspace = Path(env.get("TODO_MCP_WORKSPACE") or project_root).expanduser().resolve()
    if not workspace.is_dir():
        raise ValueError("TODO_MCP_WORKSPACE must identify an existing directory")

    configured = env.get("TODO_MCP_SERVER")
    if configured:
        server = Path(configured).expanduser().resolve()
        if not server.is_file():
            raise ValueError("TODO_MCP_SERVER must identify the extension's todo-mcp.js")
    else:
        candidates = set()
        for directory in (".cursor/extensions", ".cursor-server/extensions", ".vscode/extensions"):
            candidates.update(
                p.resolve() for p in (Path(user_home) / directory).glob("hurtis.todo-*/bin/todo-mcp.js")
                if p.is_file()
            )
        if len(candidates) != 1:
            raise ValueError("Set TODO_MCP_SERVER to the installed extension's todo-mcp.js; automatic discovery requires exactly one candidate")
        server = next(iter(candidates))

    node = shutil.which(env.get("TODO_MCP_NODE") or "node")
    if not node:
        raise ValueError("Node is unavailable; install it or set TODO_MCP_NODE")
    return [node, str(server), "--workspace", str(workspace)]


def main():
    try:
        command = resolve_command(os.environ, Path(__file__).resolve().parents[2], Path.home())
        os.execv(command[0], command)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
