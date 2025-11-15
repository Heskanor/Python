"""Compare ft_tqdm with the real tqdm implementation."""

from time import sleep

from Loading import ft_tqdm

try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover - helpful fallback
    tqdm = None


def main() -> None:
    """Run ft_tqdm and tqdm to compare outputs."""
    for _ in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    if tqdm is not None:
        for _ in tqdm(range(333)):
            sleep(0.005)
        print()
    else:
        print("tqdm is not installed; skipping comparison.")


if __name__ == "__main__":
    main()
