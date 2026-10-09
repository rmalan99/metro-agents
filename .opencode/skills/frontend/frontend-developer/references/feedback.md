# Operation feedback and ModalAlert contract

Load for create/update/delete/submit operations, backend failures or user-facing completion feedback. Use the adopted UI system's accessible modal/dialog primitive; do not introduce another UI system for feedback.

## Required channel

Use a project-owned `ModalAlert` as the primary result feedback:

| Outcome | Required presentation |
|---|---|
| Create/update/delete/submit completed | Success `ModalAlert` after authoritative completion |
| Backend or operation failure | Error `ModalAlert` with a safe, processed and actionable message |
| Backend field-validation failure | Error `ModalAlert` summary plus inline errors on the affected fields |
| Client field validation | Inline field errors; do not open a modal while typing or for each local rule |
| Persistent contextual information | Static in-page notice is allowed when it is not an operation result |

Do not use toast/snackbar or a static alert as the primary result of an operation unless the user explicitly requests that exception. Never call native JavaScript `alert()` or `window.alert()`; a browser alert is not `ModalAlert`.

## Shared component

Create or reuse one project-owned `ModalAlert`; pages and features must not assemble one-off result dialogs. Its contract includes open state, semantic variant (`success`, `error`, `warning` or `info`), concise title, processed message, close/acknowledge action, optional recovery action and stable test-ID scope. Use the adopted icon set for the variant icon.

Render backend failures in user-facing language and preserve useful actionable detail, but do not expose stack traces, raw payloads, credentials or sensitive internals. Keep the original operation state recoverable where practical. Do not report success before the authoritative operation completes.

## Modal behavior and accessibility

Use a true modal dialog with an accessible name and description, contained focus, keyboard operation, visible focus and focus return to the initiating control. Choose `dialog` or `alertdialog` semantics according to urgency; the component name alone does not justify an interruptive role. Provide an explicit close/acknowledge action and do not auto-dismiss before the user can read the result.

Do not stack duplicate result modals. Define one owner for active operation feedback and serialize or replace messages intentionally when operations can overlap. Closing a result modal must not repeat the mutation or discard recoverable form input.

## Verification

Verify success appears only after completion; backend failure uses the processed message; backend field errors appear both in the modal summary and at their fields; focus enters and returns correctly; keyboard close/acknowledge works; and no native alert, toast/snackbar or static operation-result alert remains in the affected flow. Identify modal root, title, message, icon and actions through the inherited selector contract.
