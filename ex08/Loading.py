"""Minimal tqdm-like progress bar."""

import os
from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def _progress_bar(progress: float, index: int, total: int, width: int) -> str:
    """Return a textual progress bar for the given progress ratio."""
    filled = int(progress * width)
    if filled >= width:
        bar = "=" * width
    else:
        bar = f"{'=' * filled}>{' ' * (width - filled - 1)}"
    return f"{int(progress * 100):3d}%|[{bar}]| {index}/{total}"


def ft_tqdm(lst: Iterable[T]) -> Iterator[T]:
    """Yield every element from lst while displaying a progress bar."""
    try:
        total = len(lst)  # type: ignore[arg-type]
        data_iterable = lst
    except TypeError:
        data_iterable = list(lst)
        total = len(data_iterable)
    if total == 0:
        return
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80
    width = max(1, columns - 30)
    for index, value in enumerate(data_iterable, start=1):
        progress = index / total
        print(
            f"\r{_progress_bar(progress, index, total, width)}",
            end="",
            flush=True,
        )
        yield value
    print()
