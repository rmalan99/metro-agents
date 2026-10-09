# Task quality

```yaml
quality:
  acceptance_criteria: [] # requirement/criterion IDs and observable outcomes
  risk: LOW | MEDIUM | HIGH
  write_paths: [] # explicit files or bounded directories
  read_dependencies: [] # artifacts that must remain stable during execution
  exclusive_resources: [] # ports, databases, fixtures, generated outputs
  prerequisite_acceptances: [] # accepted task IDs/evidence
  validation_plan: [] # check, working directory, expected behavior, mandatory flag
  not_applicable: [] # check and reason
```

Required alongside every development/QA task. For read-only work, write_paths is empty. validation_plan entries specify check, working_directory, expected and mandatory.
