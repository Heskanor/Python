"""Identify different null-like values."""

from math import isnan
from typing import Any


def NULL_not_found(obj: Any) -> int:
    """Print the null category of obj, return 0 on success and 1 on failure."""
    if obj is None:
        print("Nothing:", obj, type(obj))
        return 0
    if isinstance(obj, float) and isnan(obj):
        print("Cheese:", obj, type(obj))
        return 0
    if obj is False:
        print("Fake:", obj, type(obj))
        return 0
    if isinstance(obj, int) and obj == 0 and not isinstance(obj, bool):
        print("Zero:", obj, type(obj))
        return 0
    if isinstance(obj, str) and obj == "":
        print("Empty:", type(obj))
        return 0
    print("Type not found")
    return 1


if __name__ == "__main__":
    pass
