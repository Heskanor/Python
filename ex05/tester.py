"""Tester for ex05 using the long sample text from the subject."""

from building import count_characters


def main() -> None:
    """Compute and display statistics for the sample paragraph."""
    sample_text = (
        "Python 3.0, released in 2008, was a major revision that is not "
        "completely backward compatible with earlier versions. "
        "Python 2 was discontinued with version 2.7.18 in 2020."
    )
    stats = count_characters(sample_text)
    print(f"The text contains {stats['total']} characters:")
    print(f"{stats['upper']} upper letters")
    print(f"{stats['lower']} lower letters")
    print(f"{stats['punctuation']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


if __name__ == "__main__":
    main()
