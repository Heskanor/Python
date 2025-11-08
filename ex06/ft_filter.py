"""Custom implementation of Python's filter built-in."""

from collections.abc import Callable, Iterable, Iterator
from typing import Optional, TypeVar

T = TypeVar("T")


def ft_filter(
    function: Optional[Callable[[T], bool]], iterable: Iterable[T]
) -> Iterator[T]:
    """ft_filter(function or None, iterable) --> filter object."""
    predicate = function or bool
    if not callable(predicate):
        raise TypeError("ft_filter expected a callable or None as first argument")
    filtered_items = [item for item in iterable if predicate(item)]
    for item in filtered_items:
        yield item
