"""Format the current Unix timestamp in two human-friendly ways."""

from datetime import datetime
from time import time


def format_timestamp() -> tuple[str, str]:
    """Return the formatted timestamp string and the readable date."""
    current_seconds = time()

    # Format the seconds count using plain digits and scientific notation.
    fixed_number = f"{current_seconds:,.4f}"
    scientific_number = f"{current_seconds:.2e}"
    seconds_line = (
        "Seconds since January 1, 1970: "
        f"{fixed_number} or {scientific_number} in scientific notation"
    )

    # Convert the timestamp to a short date such as "Nov 12 2025".
    date_obj = datetime.fromtimestamp(current_seconds)
    formatted_date = date_obj.strftime("%b %d %Y")
    return seconds_line, formatted_date


def main() -> None:
    """Print the formatted timestamp information."""
    seconds_line, formatted_date = format_timestamp()
    print(seconds_line)
    print(formatted_date)


if __name__ == "__main__":
    main()
