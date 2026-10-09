import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("todo_bootstrap", ROOT / ".opencode/tools/run-todo-mcp.py")
bootstrap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bootstrap)


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="metro-todo-")
        self.root = Path(self.temp.name)
        self.project = self.root / "workspace with spaces"
        self.project.mkdir()
        self.home = self.root / "home"

    def tearDown(self):
        self.temp.cleanup()

    def server(self, name=".cursor/extensions/hurtis.todo-1/bin/todo-mcp.js"):
        path = self.home / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("// test fixture\n")
        return path

    @patch.object(bootstrap.shutil, "which", return_value="/usr/bin/node")
    def test_discovery_and_workspace_default_are_relocation_safe(self, _):
        server = self.server()
        command = bootstrap.resolve_command({}, self.project, self.home)
        self.assertEqual(command, ["/usr/bin/node", str(server), "--workspace", str(self.project)])

    @patch.object(bootstrap.shutil, "which", return_value="/custom/node")
    def test_explicit_server_and_workspace_overrides(self, which):
        server = self.server()
        workspace = self.root / "other workspace"
        workspace.mkdir()
        command = bootstrap.resolve_command({"TODO_MCP_SERVER": str(server), "TODO_MCP_WORKSPACE": str(workspace), "TODO_MCP_NODE": "custom-node"}, self.project, self.home)
        self.assertEqual(command, ["/custom/node", str(server), "--workspace", str(workspace)])
        which.assert_called_with("custom-node")

    @patch.object(bootstrap.shutil, "which", return_value="/usr/bin/node")
    def test_missing_or_ambiguous_installations_require_explicit_path(self, _):
        with self.assertRaisesRegex(ValueError, "exactly one"):
            bootstrap.resolve_command({}, self.project, self.home)
        self.server()
        self.server(".cursor/extensions/hurtis.todo-2/bin/todo-mcp.js")
        with self.assertRaisesRegex(ValueError, "exactly one"):
            bootstrap.resolve_command({}, self.project, self.home)

    def test_invalid_paths_and_missing_node_fail(self):
        with self.assertRaisesRegex(ValueError, "existing directory"):
            bootstrap.resolve_command({"TODO_MCP_WORKSPACE": str(self.root / "absent")}, self.project, self.home)
        with self.assertRaisesRegex(ValueError, "TODO_MCP_SERVER"):
            bootstrap.resolve_command({"TODO_MCP_SERVER": str(self.root / "absent.js")}, self.project, self.home)
        server = self.server()
        with patch.object(bootstrap.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "Node is unavailable"):
                bootstrap.resolve_command({"TODO_MCP_SERVER": str(server)}, self.project, self.home)


if __name__ == "__main__":
    unittest.main()
