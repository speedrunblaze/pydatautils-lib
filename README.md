# PyDataUtils

A simple Python library for data manipulation.

## Features

- JSON handling (save and load JSON files)
- List utilities (remove duplicates, split lists into chunks)
- String utilities (clean text, count words)

## Installation

```bash
pip install git+https://github.com/speedrunblaze/pydatautils-lib.git
```

## Usage

```python
from pydatautils.json_utils import save_json, load_json

data = {"name": "speedrunblaze", "age": 15}
save_json(data, "data.json")
print(load_json("data.json"))
```

## License

This project is licensed under the MIT License.
