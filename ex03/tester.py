"""Tester for ex03 using the sample from the subject."""

from NULL_not_found import NULL_not_found


def main() -> None:
    """Call NULL_not_found with each provided object."""
    nothing = None
    garlic = float("NaN")
    zero = 0
    empty = ""
    fake = False

    NULL_not_found(nothing)
    NULL_not_found(garlic)
    NULL_not_found(zero)
    NULL_not_found(empty)
    NULL_not_found(fake)
    print(NULL_not_found("Brian"))


if __name__ == "__main__":
    main()
