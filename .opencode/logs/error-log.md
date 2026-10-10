# Error reporting

Call `report-error` with one argument, `markdown`: free-form Markdown describing an observed incident. No event fields, IDs, timestamps or classifications are required. Preserve known facts and exact error messages; do not invent missing details or include credentials.

The tool starts a detached Python writer and returns without waiting for disk persistence. Every invocation appends to the same UTF-8 `error-log.md` in the project worktree, separating reports with a Markdown horizontal rule. A file lock serializes only the background writers to prevent interleaving. Reports never append to an internal JSONL log, read an event contract or dispatch a model/subagent. Concurrent writes preserve previous reports and never overwrite the shared file.

`QUEUED` means only that the report was handed to the background process, not that writing succeeded. `NOT_QUEUED` means launching or handing off failed. Neither outcome changes delivery status. A background filesystem failure may leave no complete report; do not wait for it, retry, ask the user for a schema or turn it into another logging incident. Mention a known failure briefly in the final result and continue independent work.

Orchestrator and team Leads report each incident once. Logging never gates refinement, frontend, backend, QA or corrections. Actual product failures and unavailable execution dependencies retain their own delivery status; reporting cannot fix those failures.
