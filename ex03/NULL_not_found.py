"""Detect and describe special null-like values."""

import math
from typing import Any


def NULL_not_found(obj: Any) -> int:
    """Print the null category of obj, returning 0 on success and 1 otherwise."""
    if obj is None:
        print(f"Nothing: None {type(obj)}")
        return 0
    if isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: nan {type(obj)}")
        return 0
    if isinstance(obj, int) and not isinstance(obj, bool) and obj == 0:
        print(f"Zero: 0 {type(obj)}")
        return 0
    if isinstance(obj, str) and obj == "":
        print(f"Empty: {type(obj)}")
        return 0
    if obj is False:
        print(f"Fake: False {type(obj)}")
        return 0
    print("Type not found")
    return 1


if __name__ == "__main__":
    pass
