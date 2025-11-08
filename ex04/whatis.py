"""Tell if a provided integer is even or odd."""

import sys


def main() -> None:
    """Entry point of program."""
    args = sys.argv[1:]
    if not args:
        return
    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        value = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    print("I'm Even." if value % 2 == 0 else "I'm Odd.")


if __name__ == "__main__":
    main()
