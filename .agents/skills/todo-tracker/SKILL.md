---
name: todo-tracker
description: View, add, update, move, and delete tasks/todos in the active project using the TODO MCP server. Use whenever the user asks to manage, add, view, complete, block, or delete TODO tasks instead of editing the .todo file directly.
---

# TODO Tracker MCP Skill

Use the [repository policy](../../../AGENTS.md) as the authority for task management. This skill owns MCP tool names/arguments only. Load it for task operations, not general development.

Invoke the configured todo-mcp (or todo-extension) tool through the active client's MCP mechanism; do not assume a generic call_mcp_tool exists in every client. Configuration guidance is in [TODO setup](../../../docs/todo-mcp.md).

## Available Tools & Exact Arguments

### 1. `todo_get_tasks`
Retrieves all tasks with IDs, categories (🔵 TODO, 🟠 Active, 🟣 Backlog, 🔴 Blocked, 🟢 Completed), and due dates. ALWAYS run this first when finding IDs to update or delete.
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_get_tasks`
- **Arguments**:
```json
{
  "category": "ALL"
}
```
*(Optional category values: "ALL", "TODO", "Active", "Backlog", "Blocked", "Completed")*

---

### 2. `todo_add_tasks`
Creates one or more new tasks.
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_add_tasks`
- **Arguments**:
```json
{
  "tasks": [
    {
      "title": "Task title here",
      "category": "TODO",
      "dueDate": "YYYY-MM-DD"
    }
  ]
}
```
*(Category options: "TODO", "Active", "Backlog", "Blocked", "Completed". dueDate is optional.)*

---

### 3. `todo_update_tasks`
Bulk updates existing tasks (e.g. move to Active, mark as Completed, change title or due date).
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_update_tasks`
- **Arguments**:
```json
{
  "updates": [
    {
      "id": "exact_task_id_from_todo_get_tasks",
      "title": "New title (optional)",
      "category": "Active",
      "dueDate": "YYYY-MM-DD"
    }
  ]
}
```

---

### 4. `todo_delete_tasks`
Deletes specific tasks by ID list.
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_delete_tasks`
- **Arguments**:
```json
{
  "ids": ["exact_task_id_1", "exact_task_id_2"]
}
```

---

### 5. `todo_clear_category`
Deletes all tasks in a category in one call (e.g. "delete all blocked tasks", "clear completed").
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_clear_category`
- **Arguments**:
```json
{
  "category": "Blocked",
  "confirm": true
}
```
*(Category options: "TODO", "Active", "Backlog", "Blocked", "Completed", "ALL". confirm must be true.)*

---

### 6. `todo_move_category`
Moves all tasks from one category to another (e.g. "move all backlog tasks to active").
- **ServerName**: `todo-mcp` *(or `todo-extension`)*
- **ToolName**: `todo_move_category`
- **Arguments**:
```json
{
  "fromCategory": "Backlog",
  "toCategory": "Active"
}
```
