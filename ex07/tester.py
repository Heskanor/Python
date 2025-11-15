"""Tester for ex07 using the sample subject cases."""

from __future__ import annotations

import subprocess
from typing import List


def run_case(args: List[str], label: str) -> None:
    """Execute sos.py with args and display the output."""
    command = ["python3", "sos.py", *args]
    print(label)
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
    print()


def main() -> None:
    """Run success and failure cases."""
    run_case(["sos"], "Valid input")
    run_case(["h$llo"], "Invalid input")


if __name__ == "__main__":
    main()
