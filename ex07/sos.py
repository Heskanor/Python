"""Encode strings to Morse code."""

import sys

MORSE_CODE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def parse_args() -> str:
    """Return the string argument or raise an AssertionError."""
    args = sys.argv[1:]
    if len(args) != 1:
        raise AssertionError("the arguments are bad")
    return args[0]


def encode_morse(text: str) -> str:
    """Encode the provided text to Morse code."""
    encoded_chars = []
    for char in text.upper():
        try:
            encoded_chars.append(MORSE_CODE[char])
        except KeyError as exc:
            raise AssertionError("the arguments are bad") from exc
    return " ".join(encoded_chars)


def main() -> None:
    """Program entry point."""
    try:
        print(encode_morse(parse_args()))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
