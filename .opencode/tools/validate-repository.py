"""Offline structural checks for the agent/skill repository; no runtime claims."""
from collections import defaultdict
from fnmatch import fnmatchcase
from pathlib import Path
import argparse
import json
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


def load_json(path):
    return json.loads(jsonc_text(path.read_text()), object_pairs_hook=unique_pairs)


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
    markdown = [p for directory in (".opencode", ".agents", ".cursor", "docs")
                for p in (root / directory).rglob("*") if p.is_file() and p.suffix in (".md", ".mdc")]
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
