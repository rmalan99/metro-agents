"""Offline structural checks for the agent/skill repository; no runtime claims."""
from collections import defaultdict
from fnmatch import fnmatchcase
from pathlib import Path
import argparse
import json
import math
import re
import sys


def jsonc_text(text):
    """Remove comments and trailing commas without altering quoted strings."""
    output = []
    i = 0
    quoted = False
    while i < len(text):
        char = text[i]
        if quoted:
            output.append(char)
            if char == "\\" and i + 1 < len(text):
                i += 1
                output.append(text[i])
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
            output.append(char)
        elif text.startswith("//", i):
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
            continue
        elif text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end < 0:
                raise ValueError("Unterminated JSONC comment")
            output.extend("\n" if c == "\n" else " " for c in text[i:end + 2])
            i = end + 2
            continue
        else:
            output.append(char)
        i += 1
    clean = "".join(output)
    output = []
    quoted = False
    i = 0
    while i < len(clean):
        char = clean[i]
        if quoted:
            output.append(char)
            if char == "\\" and i + 1 < len(clean):
                i += 1
                output.append(clean[i])
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
            output.append(char)
        elif char == "," and clean[i + 1:].lstrip().startswith(("}", "]")):
            pass
        else:
            output.append(char)
        i += 1
    return "".join(output)


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_json_constant(value):
    raise ValueError(f"Invalid JSON constant: {value}")


def load_json(path):
    return json.loads(jsonc_text(path.read_text()), object_pairs_hook=unique_pairs, parse_constant=reject_json_constant)


def prose_and_blocks(source):
    prose, blocks = [], []
    fence = None
    language = ""
    content = []
    for line in source.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is None:
            if match:
                fence, language = match.group(1), match.group(2).strip()
                content = []
                prose.append("")
            else:
                prose.append(line)
        elif match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
            blocks.append((language, "\n".join(content)))
            fence = None
        else:
            content.append(line)
    if fence:
        raise ValueError("Unclosed Markdown fence")
    return "\n".join(prose), blocks


def reference_paths(prose):
    links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", prose)
    inline = re.findall(r"`([^`\n]+\.md)`", prose)
    for value in links + inline:
        if value.startswith(("https://", "http://", "app://", "#")) or any(c in value for c in "<>*"):
            continue
        yield value.split("#", 1)[0]


def nested_value(data, dotted_path):
    value = data
    for part in dotted_path.split("."):
        if not isinstance(value, dict) or part not in value:
            raise KeyError(dotted_path)
        value = value[part]
    return value


def schema_type_matches(value, expected):
    checks = {
        "object": lambda item: isinstance(item, dict),
        "string": lambda item: isinstance(item, str),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
    }
    expected_types = expected if isinstance(expected, list) else [expected]
    if not expected_types or not all(isinstance(kind, str) for kind in expected_types):
        return False
    return any(kind in checks and checks[kind](value) for kind in expected_types)


def resolve_local_schema(schema, reference):
    if not reference.startswith("#/"):
        raise ValueError(f"unsupported schema reference {reference}")
    value = schema
    for part in reference[2:].split("/"):
        value = value[part.replace("~1", "/").replace("~0", "~")]
    return value


def schema_errors(value, rule, schema, path="$", seen=None):
    if not isinstance(rule, dict):
        return [f"{path}: schema rule must be an object"]
    seen = set() if seen is None else seen
    marker = (id(value), id(rule))
    if marker in seen:
        return [f"{path}: cyclic schema reference"]
    seen.add(marker)
    if "$ref" in rule:
        if not isinstance(rule["$ref"], str):
            return [f"{path}: schema reference must be a string"]
        try:
            target = resolve_local_schema(schema, rule["$ref"])
        except (KeyError, TypeError, ValueError) as exc:
            return [f"{path}: {exc}"]
        return schema_errors(value, target, schema, path, seen)
    if "anyOf" in rule:
        if not isinstance(rule["anyOf"], list) or not rule["anyOf"] or not all(isinstance(item, dict) for item in rule["anyOf"]):
            return [f"{path}: anyOf must be a non-empty rule list"]
        alternatives = [schema_errors(value, option, schema, path, set(seen)) for option in rule["anyOf"]]
        if not any(not errors for errors in alternatives):
            return [f"{path}: does not match any allowed schema"]
    errors = []
    if "const" in rule and value != rule["const"]:
        errors.append(f"{path}: must equal {rule['const']!r}")
    if "type" in rule and not schema_type_matches(value, rule["type"]):
        return errors + [f"{path}: invalid type"]
    if isinstance(value, dict):
        required = rule.get("required", [])
        properties = rule.get("properties", {})
        additional = rule.get("additionalProperties", True)
        if not isinstance(required, list) or not all(isinstance(key, str) for key in required):
            return errors + [f"{path}: required must be a string list"]
        if not isinstance(properties, dict):
            return errors + [f"{path}: properties must be an object"]
        if not isinstance(additional, (bool, dict)):
            return errors + [f"{path}: additionalProperties must be a boolean or rule"]
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key}")
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in properties:
                errors.extend(schema_errors(child, properties[key], schema, child_path, set(seen)))
            elif additional is False:
                errors.append(f"{child_path}: additional property is not allowed")
            elif isinstance(additional, dict):
                errors.extend(schema_errors(child, additional, schema, child_path, set(seen)))
        min_properties = rule.get("minProperties", 0)
        if not isinstance(min_properties, int) or isinstance(min_properties, bool) or min_properties < 0:
            return errors + [f"{path}: minProperties must be a non-negative integer"]
        if len(value) < min_properties:
            errors.append(f"{path}: too few properties")
    if isinstance(value, str):
        min_length = rule.get("minLength", 0)
        if not isinstance(min_length, int) or isinstance(min_length, bool) or min_length < 0:
            return errors + [f"{path}: minLength must be a non-negative integer"]
        if len(value) < min_length:
            errors.append(f"{path}: string is too short")
        if "pattern" in rule:
            if not isinstance(rule["pattern"], str):
                return errors + [f"{path}: pattern must be a string"]
            try:
                matches = re.search(rule["pattern"], value)
            except re.error as exc:
                return errors + [f"{path}: invalid pattern: {exc}"]
            if not matches:
                errors.append(f"{path}: does not match required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = rule.get("minimum", value)
        if not isinstance(minimum, (int, float)) or isinstance(minimum, bool) or not math.isfinite(minimum):
            return errors + [f"{path}: minimum must be a finite number"]
        if not math.isfinite(value):
            errors.append(f"{path}: number must be finite")
        elif value < minimum:
            errors.append(f"{path}: value is below minimum")
    return errors


def validate_ui_system(root):
    errors = []
    base = root / ".opencode/skills/frontend/ui-system-architect"
    tokens_path = base / "assets/tokens.json"
    schema_path = base / "assets/tokens.schema.json"
    if not base.is_dir():
        return errors
    try:
        tokens = load_json(tokens_path)
        schema = load_json(schema_path)
    except (ValueError, OSError) as exc:
        return [f"ui-system-architect assets: {exc}"]
    if not isinstance(tokens, dict) or not isinstance(schema, dict):
        return ["ui-system-architect assets: tokens and schema roots must be objects"]
    errors.extend(f"ui-system-architect schema: {error}" for error in schema_errors(tokens, schema, schema))
    if tokens.get("$schema") != "./tokens.schema.json":
        errors.append("ui-system-architect tokens: invalid schema reference")

    required_paths = (
        "color.semantic.canvas",
        "color.semantic.surface",
        "color.semantic.text",
        "color.semantic.border",
        "color.semantic.primary",
        "color.semantic.focus",
        "control.hitArea.minimum",
        "component.button.md",
        "component.input.md",
        "component.select.menu",
        "component.card",
        "component.modal",
        "component.table",
        "component.selection",
        "component.badge",
        "component.alert",
        "component.drawer",
        "component.tooltip",
        "component.menu",
        "component.tabs",
        "component.pagination",
        "component.navigation",
        "component.feedback",
        "component.avatar",
        "component.file",
        "composition.formField",
        "composition.formSection",
        "composition.pageHeader",
        "composition.filterBar",
        "composition.dataTableLayout",
        "layout.shell",
        "layout.page",
        "grid",
        "breakpoint",
    )
    for path in required_paths:
        try:
            nested_value(tokens, path)
        except KeyError:
            errors.append(f"ui-system-architect tokens: missing required path {path}")

    token_reference = re.compile(r"\{([a-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+)\}")
    for path in (base / "references").rglob("*.md"):
        try:
            source = path.read_text()
        except OSError as exc:
            errors.append(f"{path.relative_to(root).as_posix()}: {exc}")
            continue
        for token_path in token_reference.findall(source):
            try:
                nested_value(tokens, token_path)
            except KeyError:
                relative = path.relative_to(root).as_posix()
                errors.append(f"{relative}: unknown UI token {token_path}")

    try:
        minimum_hit_area = int(nested_value(tokens, "control.hitArea.minimum").removesuffix("px"))
        breakpoints = [int(tokens["breakpoint"][key].removesuffix("px")) for key in ("sm", "md", "lg", "xl")]
    except (AttributeError, KeyError, TypeError, ValueError):
        errors.append("ui-system-architect tokens: invalid px sizing value")
    else:
        if minimum_hit_area < 40:
            errors.append("ui-system-architect tokens: minimum hit area must be at least 40px")
        if breakpoints != sorted(set(breakpoints)):
            errors.append("ui-system-architect tokens: breakpoints must be strictly increasing")
    return errors


def action_for(rules, path):
    if isinstance(rules, str):
        return rules
    action = "deny"
    for pattern, value in rules.items():
        if fnmatchcase(path, pattern):
            action = value
    return action


def validate(root):
    root = Path(root).resolve()
    errors = []
    try:
        config = load_json(root / "opencode.jsonc")
        registry = load_json(root / ".opencode/skill-ownership.json")
        cursor = load_json(root / ".cursor/mcp.json")
    except (ValueError, OSError) as exc:
        return [str(exc)]
    ignored_parts = {"node_modules", "work", "__pycache__"}
    markdown = [p for directory in (".opencode", ".agents", ".cursor", "docs")
                for p in (root / directory).rglob("*")
                if p.is_file() and p.suffix in (".md", ".mdc")
                and not ignored_parts.intersection(p.relative_to(root).parts)]
    markdown += [p for p in root.glob("*.md")]
    paragraphs = defaultdict(set)
    skills = {}
    schema_dir = root / ".opencode/skills/hierarchical-software-delivery/references/schemas"
    artifact_keys = set(registry["artifacts"].values())
    schema_blocks = {}
    for path in markdown:
        relative = path.relative_to(root).as_posix()
        try:
            source = path.read_text()
            prose, blocks = prose_and_blocks(source)
        except (ValueError, OSError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        if path.name == "SKILL.md":
            header = re.match(r"\A---\n(.*?)\n---\n", source, re.S)
            name = re.search(r"^name: ([a-z0-9-]+)$", header.group(1), re.M) if header else None
            description = re.search(r"^description: .+", header.group(1), re.M) if header else None
            if not name or not description or name.group(1) != path.parent.name:
                errors.append(f"{relative}: invalid skill metadata/directory identity")
            elif name.group(1) in skills:
                errors.append(f"{relative}: duplicate skill name {name.group(1)}")
            else:
                skills[name.group(1)] = relative
        for ref in reference_paths(prose):
            target = (root / ref) if ref.startswith((".opencode/", ".agents/", ".cursor/")) else (path.parent / ref)
            if not target.is_file():
                errors.append(f"{relative}: missing reference {ref}")
        for paragraph in re.split(r"\n\s*\n", prose):
            normalized = " ".join(paragraph.split())
            if len(normalized.split()) >= 25:
                paragraphs[normalized].add(relative)
        for language, body in blocks:
            if language == "yaml":
                defined = set(re.findall(r"^([a-z_]+):", body, re.M)) & artifact_keys
                if re.search(r"^- check:", body, re.M):
                    defined.add("- check")
                if defined and path.parent != schema_dir:
                    errors.append(f"{relative}: artifact definition outside its canonical schema: {sorted(defined)}")
                if path.parent == schema_dir:
                    if relative in schema_blocks:
                        errors.append(f"{relative}: multiple YAML definitions in one canonical schema")
                    else:
                        schema_blocks[relative] = body
    for paragraph, paths in paragraphs.items():
        if len(paths) > 1:
            errors.append(f"Duplicated prose (25+ words) in {', '.join(sorted(paths))}: {paragraph[:65]}")
    for family, relative in registry["rules"].items():
        if not (root / relative).is_file():
            errors.append(f"Rule {family}: missing owner {relative}")
    for relative, key in registry["artifacts"].items():
        body = schema_blocks.get(relative)
        if body is None or not re.search(r"^" + re.escape(key) + r":", body, re.M):
            errors.append(f"Artifact {key}: missing canonical definition in {relative}")
    if set(schema_blocks) != set(registry["artifacts"]):
        errors.append("Schema catalog and artifact ownership registry differ")
    errors.extend(validate_ui_system(root))
    agents = config.get("agent", {})
    for name, agent in agents.items():
        match = re.fullmatch(r"\{file:(.+)\}", agent.get("prompt", ""))
        if not match or not (root / match.group(1)).is_file():
            errors.append(f"Agent {name}: missing prompt")
        permissions = agent.get("permission", {})
        for kind, available in (("task", agents), ("skill", skills)):
            rules = permissions.get(kind, {})
            if isinstance(rules, dict):
                for target, value in rules.items():
                    if target != "*" and value == "allow" and target not in available:
                        errors.append(f"Agent {name}: unknown allowed {kind} {target}")
    for name in ("frontend-lead", "frontend-junior"):
        rules = agents.get(name, {}).get("permission", {}).get("skill", {})
        for skill in skills:
            if skills[skill].startswith(".opencode/skills/frontend/") and action_for(rules, skill) != "allow":
                errors.append(f"Agent {name}: cannot load frontend skill {skill}")
    for name in ("orchestrator", "evaluator"):
        rules = agents.get(name, {}).get("permission", {}).get("read", {})
        if not isinstance(rules, dict) or rules.get("*") != "deny":
            errors.append(f"Agent {name}: contract reads must default deny")
            continue
        for path in registry["restricted_reads"][name]:
            for candidate in (path, (root / path).as_posix()):
                if action_for(rules, candidate) != "allow":
                    errors.append(f"Agent {name}: cannot read required contract {path}")
        for pattern, value in rules.items():
            if value == "allow" and pattern.removeprefix("*/") not in registry["restricted_reads"][name]:
                errors.append(f"Agent {name}: unexpected allowed read {pattern}")
        for candidate in ("src/main.tsx", (root / "src/main.tsx").as_posix()):
            if action_for(rules, candidate) != "deny":
                errors.append(f"Agent {name}: source reads must remain denied")
    for name, allowed in registry["dispatch"].items():
        rules = agents.get(name, {}).get("permission", {}).get("task", {})
        actual = {k for k, v in rules.items() if v == "allow"} if isinstance(rules, dict) else set()
        if actual != set(allowed) or (isinstance(rules, dict) and rules.get("*") != "deny"):
            errors.append(f"Agent {name}: delegation differs from canonical role scope")
    logger_command = "python3 .opencode/tools/append-error-log.py"
    logger_command_with_input = logger_command + " <<'JSON'"
    for name, agent in agents.items():
        bash = agent.get("permission", {}).get("bash", "deny")
        expected = "allow" if name == "error-logger" else "deny"
        for command in (logger_command, logger_command_with_input):
            if action_for(bash, command) != expected:
                errors.append(f"Agent {name}: error-log writer permission must be {expected}")
                break
    logger_bash = agents.get("error-logger", {}).get("permission", {}).get("bash", {})
    expected_logger_bash = {
        "*": "deny",
        logger_command: "allow",
        logger_command + " *": "allow",
    }
    if not isinstance(logger_bash, dict) or logger_bash != expected_logger_bash:
        errors.append("Agent error-logger: bash scope must contain only the append helper")
    todo = cursor.get("mcpServers", {}).get("todo-mcp", {})
    if todo.get("command") != "python3" or todo.get("args") != [".opencode/tools/run-todo-mcp.py"]:
        errors.append("Cursor TODO MCP must use the portable bootstrap")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} validation error(s)", file=sys.stderr)
        return 1
    print("PASS: metadata, references, ownership, canonical artifacts, prose, routing and restricted reads")
    print("Static checks only; runtime permission enforcement, models and concurrency are not verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
