"""Say whether the provided integer is odd or even."""

import sys


def is_integer(text: str) -> bool:
    """Return True if text represents an integer (supports negatives)."""
    if text.startswith("-"):
        return text[1:].isdigit()
    return text.isdigit()


def main() -> None:
    """Check the argument and print whether it is odd or even."""
    args = sys.argv[1:]
    if not args:
        return
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return
    value = args[0]
    if not is_integer(value):
        print("AssertionError: argument is not an integer")
        return
    number = int(value)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
