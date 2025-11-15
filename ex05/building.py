"""Count different character categories in a text."""

import string
import sys
from typing import Dict


def count_characters(text: str) -> Dict[str, int]:
    """Return statistics on the provided text."""
    stats = {
        "total": len(text),
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }
    # Walk through every character once and update the matching counters.
    for char in text:
        if char.isupper():
            stats["upper"] += 1
        elif char.islower():
            stats["lower"] += 1
        if char in string.punctuation:
            stats["punctuation"] += 1
        if char.isspace():
            stats["spaces"] += 1
        if char.isdigit():
            stats["digits"] += 1
    return stats


def read_text(args: list[str]) -> str:
    """Return the text to analyze, prompting the user if necessary."""
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    if args:
        return args[0]
    print("What is the text to count?")
    # readline() keeps the trailing newline so it counts as a space character.
    return sys.stdin.readline()


def main() -> None:
    """Handle CLI parsing and output the formatted statistics."""
    try:
        text = read_text(sys.argv[1:])
        stats = count_characters(text)
        print(f"The text contains {stats['total']} characters:")
        print(f"{stats['upper']} upper letters")
        print(f"{stats['lower']} lower letters")
        print(f"{stats['punctuation']} punctuation marks")
        print(f"{stats['spaces']} spaces")
        print(f"{stats['digits']} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
