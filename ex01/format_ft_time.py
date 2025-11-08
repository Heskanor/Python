from datetime import datetime
from time import time


def main() -> None:
    """Print the current timestamp with fixed and scientific formats."""
    seconds = time()
    fixed = f"{seconds:,.4f}"
    scientific = f"{seconds:.2e}"
    print(
        f"Seconds since January 1, 1970: {fixed} or {scientific} in scientific notation"
    )
    print(datetime.fromtimestamp(seconds).strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
