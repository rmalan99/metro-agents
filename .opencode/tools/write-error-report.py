"""Append plain Markdown to the single report file in a detached process."""
import fcntl
import os
from pathlib import Path
import sys


def write_report(markdown, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Only background writers wait for this lock, never the delivery caller.
    with path.open("a", encoding="utf-8") as report:
        fcntl.flock(report, fcntl.LOCK_EX)
        report.seek(0, os.SEEK_END)
        if report.tell():
            report.write("\n\n---\n\n")
        report.write(markdown)
        report.flush()
        os.fsync(report.fileno())


if __name__ == "__main__":
    try:
        write_report(sys.stdin.read(), Path(sys.argv[1]))
    except (OSError, ValueError, IndexError) as error:
        print(f"Report not written: {error}", file=sys.stderr)
        sys.exit(1)
