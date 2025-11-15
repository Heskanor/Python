"""Run sample command-line tests for ex04."""

from __future__ import annotations

import subprocess
from typing import List


def run_case(args: List[str]) -> None:
    """Execute whatis.py with the given arguments and print the result."""
    command = ["python3", "whatis.py", *args]
    print("$", " ".join(command))
    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.stderr:
        print(completed.stderr.rstrip())
    if not completed.stdout and not completed.stderr:
        print("<no output>")
    print()


def main() -> None:
    """Run the sample cases from the subject."""
    cases = [
        [],
        ["14"],
        ["-5"],
        ["0"],
        ["Hi!"],
        ["13", "5"],
    ]
    for args in cases:
        run_case(args)


if __name__ == "__main__":
    main()
