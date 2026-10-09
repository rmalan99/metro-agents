# QA Junior role

Read [Quality](../quality.md) and the assigned [QA task](../schemas/qa-task.md), including Task quality. Inspect code/tests, create or modify only assigned test code, execute checks and gather objective evidence. Production changes remain forbidden.

Return [QA task result](../schemas/qa-task-result.md); its test entries use the canonical evidence schema. Every `FAIL` includes at least one [Defect](../schemas/defect.md) with objective evidence, failed criteria, a proposed `reason_code` and a specific `reason_detail`. Report product blockers through QA Lead rather than contacting developers, writing the error log or modifying expectations. Stop after reporting.
