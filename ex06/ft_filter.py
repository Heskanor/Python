"""Custom implementation of Python's filter built-in."""

from collections.abc import Callable, Iterable, Iterator
from typing import Optional, TypeVar

T = TypeVar("T")


def ft_filter(
    function: Optional[Callable[[T], bool]], iterable: Iterable[T]
) -> Iterator[T]:
    """ft_filter(function or None, iterable) --> filter object."""
    if function is None:
        predicate = bool
    elif callable(function):
        predicate = function
    else:
        raise TypeError(
            "ft_filter expected a callable or None as first argument"
        )

    result: list[T] = []
    for item in iterable:
        if predicate(item):
            result.append(item)
    return iter(result)
