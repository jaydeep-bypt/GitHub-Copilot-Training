

# Project Task: Week 4 — Unit Testing with Copilot

> **Prompt Used:**
> 
> Create a complete Python project with a module, professional unit tests, edge cases, mocks, table-driven testing, and a README that documents everything.
> 
> **Requirements:**
> - Python module (`my_module.py`) with:
>   - `parse_string(s: str) -> list`: Parses a string into individual words and returns a list.
>   - `calculate_sum(a: int, b: int) -> int`: Returns the sum of two integers.
>   - `fetch_user_data(user_id: int) -> dict`: Fetches user data from the API endpoint: https://jsonplaceholder.typicode.com/users/{user_id}
> - Unit test suite (`tests/test_my_module.py`) using pytest:
>   - Cover normal and edge cases for all functions
>   - Use table-driven testing (`pytest.mark.parametrize`)
>   - Use `unittest.mock` to mock API calls
>   - Achieve at least 80% code coverage
> - Professional README with:
>   - Project title and description
>   - Overview of the module and functions with example usage
>   - Instructions for running tests and generating coverage reports
>   - This Copilot prompt for transparency
> - Well-formatted, maintainable, and ready-to-submit code and tests

---

# Unit Testing with Copilot

## Overview
This project demonstrates professional Python development and unit testing practices using GitHub Copilot. It includes a simple module with three functions, comprehensive unit tests (including edge cases, mocks, and table-driven testing), and clear documentation.

---

## Module: `my_module.py`

### Function Reference

#### `parse_string(s: str) -> list`
Parses a string into individual words and returns a list.

**Example:**
```python
from my_module import parse_string
print(parse_string("hello world"))  # Output: ['hello', 'world']
```

#### `calculate_sum(a: int, b: int) -> int`
Returns the sum of two integers.

**Example:**
```python
from my_module import calculate_sum
print(calculate_sum(2, 3))  # Output: 5
```

#### `fetch_user_data(user_id: int) -> dict`
Fetches user data from the API endpoint: https://jsonplaceholder.typicode.com/users/{user_id}

**Example:**
```python
from my_module import fetch_user_data
user = fetch_user_data(1)
print(user['name'])  # Output: 'Leanne Graham' (example)
```

---

## Testing & Coverage

### Prerequisites
- Python 3.7+
- [pytest](https://pytest.org/)
- [requests](https://pypi.org/project/requests/)
- [coverage](https://pypi.org/project/coverage/)

### Install Dependencies
```bash
pip install pytest requests coverage
```

### Run Tests
```bash
pytest
```


### Generate Coverage Report
```bash
coverage run -m pytest
coverage report -m
```

#### Example Coverage Report Output
```
Name            Stmts   Miss  Cover
-----------------------------------
my_module.py       12      0   100%
test_my_module.py  29      0   100%
-----------------------------------
TOTAL              41      0   100%
```

**Coverage Report Columns:**
- **Stmts**: Number of executable statements in the file.
- **Miss**: Number of statements not executed by the tests (missed).
- **Cover**: Percentage of statements executed (coverage).

---

## Project Structure
```
project/
├── my_module.py
├── README.md
└── tests/
    └── test_my_module.py
```

---

## License
This project is for educational and demonstration purposes.
