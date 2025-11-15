"""Identify the type of any object."""

from typing import Any


def all_thing_is_obj(obj: Any) -> int:
    """Print the type of the provided object and always return 42."""
    if isinstance(obj, list):
        print("List :", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple :", type(obj))
    elif isinstance(obj, set):
        print("Set :", type(obj))
    elif isinstance(obj, dict):
        print("Dict :", type(obj))
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen :", type(obj))
    else:
        print("Type not found")
    return 42


if __name__ == "__main__":
    pass
