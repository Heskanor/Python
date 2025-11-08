"""Filter words longer than a provided length."""

import sys
from typing import List

from ft_filter import ft_filter


def parse_args() -> tuple[str, int]:
    """Validate CLI arguments and return the text plus threshold."""
    args = sys.argv[1:]
    if len(args) != 2:
        raise AssertionError("the arguments are bad")
    text, raw_threshold = args
    if any(not (char.isalpha() or char.isspace()) for char in text):
        raise AssertionError("the arguments are bad")
    try:
        threshold = int(raw_threshold)
    except ValueError as exc:
        raise AssertionError("the arguments are bad") from exc
    return text, threshold


def _extract_words(text: str) -> list[str]:
    """Return words preserving single trailing spaces if present."""
    words: list[str] = []
    current = ""
    for char in text:
        current += char
        if char == " ":
            if current.strip():
                words.append(current)
            current = ""
    if current.strip():
        words.append(current)
    return words


def filter_words(text: str, limit: int) -> List[str]:
    """Return the list of words longer than limit."""
    words = [word for word in _extract_words(text)]
    condition = lambda word: len(word.strip()) > limit  # noqa: E731
    return list(ft_filter(condition, words))


def main() -> None:
    """Program entry point."""
    try:
        text, limit = parse_args()
        print(filter_words(text, limit))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
