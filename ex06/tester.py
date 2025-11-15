"""Tester for ex06 covering ft_filter and filterstring."""

from __future__ import annotations

import subprocess

from ft_filter import ft_filter


def test_ft_filter() -> None:
    """Compare ft_filter with the built-in filter on a simple example."""
    numbers = [0, 1, 2, 3, 4, 5]

    def is_even(num: int) -> bool:
        return num % 2 == 0

    original = list(filter(is_even, numbers))
    custom = list(ft_filter(is_even, numbers))
    print("Built-in filter :", original)
    print("ft_filter       :", custom)
    print("Same result?    :", original == custom)
    print()


def test_filterstring() -> None:
    """Run filterstring.py with the sample subject cases."""
    cases = [
        (["Hello the World ", "4"], "Expected: ['Hello ', 'World ']"),
        (["Hello the World ", "99"], "Expected: []"),
        (["3", "Hello the World "], "Assertion case"),
    ]
    for args, label in cases:
        command = ["python3", "filterstring.py", *args]
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
    """Run both test suites."""
    test_ft_filter()
    test_filterstring()


if __name__ == "__main__":
    main()
