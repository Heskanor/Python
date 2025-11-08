"""Counting helpers for ft_package."""

from collections.abc import Iterable
from typing import Any


def count_in_list(items: Iterable[Any], target: Any) -> int:
    """Count how many times target appears inside items."""
    return sum(1 for element in items if element == target)
