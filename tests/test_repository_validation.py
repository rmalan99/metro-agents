import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("repository_validator", ROOT / ".opencode/tools/validate-repository.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class JsoncTests(unittest.TestCase):
    def test_comments_trailing_commas_and_quoted_content(self):
        source = r'''{
          // comment
          "url": "https://example.test/a/*literal*/",
          "quoted": "value \" ,] // literal",
          "list": [1, 2, /* comment */],
        }'''
        parsed = json.loads(validator.jsonc_text(source))
        self.assertEqual(parsed["url"], "https://example.test/a/*literal*/")
        self.assertEqual(parsed["list"], [1, 2])
        self.assertIn(",] // literal", parsed["quoted"])

    def test_reject_duplicate_keys_and_unterminated_comments(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            json.loads('{"a": 1, "a": 2}', object_pairs_hook=validator.unique_pairs)
        with self.assertRaisesRegex(ValueError, "Unterminated"):
            validator.jsonc_text('{/* invalid')

    def test_longer_markdown_fence_does_not_close_on_inner_example(self):
        prose, blocks = validator.prose_and_blocks("Before\n````md\n```ts\nx\n```\n````\nAfter")
        self.assertEqual(len(blocks), 1)
        self.assertIn("Before", prose)
        self.assertIn("After", prose)


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="metro-validator-")
        cls.fixture = Path(cls.temp.name) / "repo"
        shutil.copytree(ROOT, cls.fixture, ignore=shutil.ignore_patterns(".git", "work", "__pycache__"))

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def mutate(self, relative, source, expected):
        path = self.fixture / relative
        old = path.read_text() if path.exists() else None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source)
        try:
            errors = validator.validate(self.fixture)
            self.assertTrue(any(expected in error for error in errors), errors)
        finally:
            if old is None:
                path.unlink()
            else:
                path.write_text(old)

    def config_change(self, change, expected):
        config = validator.load_json(self.fixture / "opencode.jsonc")
        change(config)
        self.mutate("opencode.jsonc", json.dumps(config), expected)

    def test_current_repository_and_relocated_fixture_pass(self):
        self.assertEqual(validator.validate(ROOT), [])
        self.assertEqual(validator.validate(self.fixture), [])

    def test_missing_reference_fails(self):
        self.mutate("docs/invalid-reference.md", "Read [missing](absent.md).\n", "missing reference")

    def test_unclosed_code_fence_fails(self):
        self.mutate("docs/invalid-fence.md", "```ts\nconst a = 1;\n", "Unclosed Markdown fence")

    def test_duplicate_skill_identity_fails(self):
        existing = (self.fixture / ".opencode/skills/frontend/frontend-forms/SKILL.md").read_text()
        self.mutate(".agents/skills/frontend-forms/SKILL.md", existing, "duplicate skill name")

    def test_long_duplicate_prose_fails(self):
        source = (self.fixture / ".opencode/skills/frontend/frontend-developer/references/test-identifiers.md").read_text()
        self.mutate("docs/duplicated-guidance.md", source, "Duplicated prose")

    def test_artifact_copy_in_prompt_fails(self):
        source = (self.fixture / ".opencode/skills/hierarchical-software-delivery/references/schemas/development-result.md").read_text()
        self.mutate(".opencode/prompts/backend-junior.md", source, "artifact definition outside")

    def test_copied_evidence_list_is_also_rejected(self):
        source = (self.fixture / ".opencode/skills/hierarchical-software-delivery/references/schemas/validation-evidence.md").read_text()
        self.mutate(".opencode/prompts/backend-junior.md", source, "artifact definition outside")

    def test_multiple_schema_definitions_in_one_file_fail(self):
        relative = ".opencode/skills/hierarchical-software-delivery/references/schemas/development-result.md"
        source = (self.fixture / relative).read_text()
        self.mutate(relative, source + "\n```yaml\ntask_result:\n  status: COMPLETED\n```\n", "multiple YAML definitions")

    def test_unknown_agent_and_skill_targets_fail(self):
        self.config_change(lambda c: c["agent"]["orchestrator"]["permission"]["task"].update({"absent": "allow"}), "unknown allowed task")
        self.config_change(lambda c: c["agent"]["frontend-junior"]["permission"]["skill"].update({"absent": "allow"}), "unknown allowed skill")

    def test_missing_frontend_skill_permission_fails(self):
        self.config_change(lambda c: c["agent"]["frontend-junior"]["permission"]["skill"].update({"frontend-forms": "deny"}), "cannot load frontend skill")

    def test_contract_read_denial_and_source_access_regressions_fail(self):
        self.config_change(lambda c: c["agent"]["evaluator"]["permission"].update({"read": "deny"}), "contract reads must default deny")
        self.config_change(lambda c: c["agent"]["evaluator"]["permission"]["read"].update({"src/*": "allow"}), "unexpected allowed read")
        self.config_change(lambda c: c["agent"]["evaluator"]["permission"]["read"].update({"*": "allow"}), "contract reads must default deny")

    def test_direct_development_junior_dispatch_is_rejected(self):
        self.config_change(lambda c: c["agent"]["orchestrator"]["permission"]["task"].update({"frontend-junior": "allow"}), "delegation differs")

    def test_leads_must_be_able_to_report_directly_to_error_logger(self):
        for lead in ("frontend-lead", "backend-lead", "qa-lead"):
            with self.subTest(lead=lead):
                self.config_change(lambda c, name=lead: c["agent"][name]["permission"]["task"].update({"error-logger": "deny"}), "delegation differs")

    def test_error_logger_is_the_only_append_helper_writer(self):
        command = "python3 .opencode/tools/append-error-log.py"
        self.config_change(lambda c: c["agent"]["qa-lead"]["permission"]["bash"].update({command: "allow"}), "writer permission must be deny")
        self.config_change(lambda c: c["agent"]["error-logger"]["permission"]["bash"].pop(command + " *"), "writer permission must be allow")
        self.config_change(lambda c: c["agent"]["error-logger"]["permission"]["bash"].update({"python3 other.py": "allow"}), "bash scope must contain only")

    def test_missing_owner_and_schema_definition_fail(self):
        registry = validator.load_json(self.fixture / ".opencode/skill-ownership.json")
        registry["rules"]["frontend.forms"] = "missing.md"
        self.mutate(".opencode/skill-ownership.json", json.dumps(registry), "missing owner")
        self.mutate(".opencode/skills/hierarchical-software-delivery/references/schemas/task-quality.md", "# No schema\n", "missing canonical definition")

    def test_qa_contract_persists_valuable_manual_cases(self):
        base = self.fixture / ".opencode/skills/hierarchical-software-delivery/references"
        quality = (base / "quality.md").read_text()
        junior = (base / "roles/qa-junior.md").read_text()
        task = (base / "schemas/qa-task.md").read_text()
        task_result = (base / "schemas/qa-task-result.md").read_text()
        qa_result = (base / "schemas/qa-result.md").read_text()

        self.assertIn("Every valuable manual case must be covered", quality)
        self.assertIn("Do not return `PASS` with uncovered valuable cases", junior)
        self.assertIn("existing_coverage: []", task)
        self.assertIn("existing_tests_reused: []", task_result)
        self.assertIn("valuable_manual_cases: []", task_result)
        self.assertIn("tests_reused: []", qa_result)
        self.assertIn("`PASSED` is invalid while any valuable case remains uncovered", qa_result)

    def test_personal_cursor_bootstrap_is_rejected(self):
        source = json.dumps({"mcpServers": {"todo-mcp": {"command": "node", "args": ["/home/person/server.js"]}}})
        self.mutate(".cursor/mcp.json", source, "portable bootstrap")


if __name__ == "__main__":
    unittest.main()
