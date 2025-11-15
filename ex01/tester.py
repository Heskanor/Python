"""Run the ex01 script and display the formatted timestamp."""

from format_ft_time import format_timestamp


def main() -> None:
    """Print the formatted timestamp twice to mirror the exercise script."""
    seconds_line, formatted_date = format_timestamp()
    print(seconds_line)
    print(formatted_date)


if __name__ == "__main__":
    main()
