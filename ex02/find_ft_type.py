"""Basic utilities to inspect python objects."""

from typing import Any


def all_thing_is_obj(obj: Any) -> int:
    """Print the object category and always return 42."""
    match obj:
        case list():
            print(f"List : {type(obj)}")
        case tuple():
            print(f"Tuple : {type(obj)}")
        case set():
            print(f"Set : {type(obj)}")
        case dict():
            print(f"Dict : {type(obj)}")
        case str():
            print(f"{obj} is in the kitchen : {type(obj)}")
        case _:
            print("Type not found")
    return 42


if __name__ == "__main__":
    pass
