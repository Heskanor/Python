# ft_package

Sample Python package used for the Piscine exercises. It exposes a single
function, `count_in_list`, that counts how many times a value appears in an
iterable.

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
```

## Development

Build the distribution:

```bash
python -m build
```

The resulting archives can be installed with `pip install dist/<archive>`.
