"""Count different character categories in a text."""

import string
import sys
from typing import Dict


def count_characters(text: str) -> Dict[str, int]:
    """Return statistics on the provided text."""
    punct_set = set(string.punctuation)
    stats = {
        "total": len(text),
        "upper": sum(1 for char in text if char.isupper()),
        "lower": sum(1 for char in text if char.islower()),
        "punctuation": sum(1 for char in text if char in punct_set),
        "spaces": sum(1 for char in text if char.isspace()),
        "digits": sum(1 for char in text if char.isdigit()),
    }
    return stats


def read_text(args: list[str]) -> str:
    """Return the text to analyze, prompting the user if necessary."""
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    if args:
        return args[0]
    print("What is the text to count?")
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
