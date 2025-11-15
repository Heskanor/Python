"""Filter words longer than a provided length."""

import sys
from typing import List

from ft_filter import ft_filter


def read_arguments() -> tuple[str, int]:
    """Return the text and length limit after basic validation."""
    args = sys.argv[1:]
    if len(args) != 2:
        raise AssertionError("the arguments are bad")
    text, limit_text = args
    for char in text:
        if not (char.isalpha() or char.isspace()):
            raise AssertionError("the arguments are bad")
    if limit_text.startswith("-"):
        digits = limit_text[1:]
    else:
        digits = limit_text
    if not digits.isdigit():
        raise AssertionError("the arguments are bad")
    return text, int(limit_text)


def split_words(text: str) -> list[str]:
    """Separate the text into words while keeping single trailing spaces."""
    words: list[str] = []
    current = ""
    for char in text:
        current += char
        if char == " " and current.strip():
            words.append(current)
            current = ""
    if current.strip():
        words.append(current)
    return words


def filter_words(text: str, limit: int) -> List[str]:
    """Return the list of words longer than limit."""
    words = [word for word in split_words(text)]
    is_long_enough = lambda word: len(word.strip()) > limit  # noqa: E731
    return list(ft_filter(is_long_enough, words))


def main() -> None:
    """Program entry point."""
    try:
        text, limit = read_arguments()
        print(filter_words(text, limit))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
