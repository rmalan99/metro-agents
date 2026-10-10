import { tool } from "@opencode-ai/plugin"
import { spawn } from "node:child_process"
import { join } from "node:path"

export default tool({
  description: "Write a simple Markdown incident in the background. No event schema or logging subagent; never gates delivery.",
  args: {
    markdown: tool.schema.string().describe("Observed incident as plain Markdown. Include only known facts; no required fields."),
  },
  async execute({ markdown }, context) {
    if (!markdown.trim()) return "NOT_QUEUED: empty report; continue delivery."
    const root = context.worktree || context.directory
    const output = join(root, "error-log.md")
    try {
      return await new Promise<string>((resolve) => {
        const child = spawn("python3", [join(root, ".opencode/tools/write-error-report.py"), output], {
          cwd: root,
          detached: true,
          stdio: ["pipe", "ignore", "ignore"],
        })
        child.on("error", (error) => resolve(`NOT_QUEUED: ${error.message}; continue delivery.`))
        child.stdin.on("error", (error) => resolve(`NOT_QUEUED: ${error.message}; continue delivery.`))
        child.once("spawn", () => {
          child.stdin.end(markdown, "utf8", () => {
            child.unref()
            resolve(`QUEUED: ${output}. Persistence is unverified; continue delivery immediately.`)
          })
        })
      })
    } catch (error) {
      return `NOT_QUEUED: ${String(error)}; continue delivery.`
    }
  },
})
