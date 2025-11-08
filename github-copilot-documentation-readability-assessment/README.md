# Python Utils Module

A comprehensive utility module for common programming tasks including string manipulation, date handling, and text processing. This module provides clean, well-documented functions that simplify everyday development tasks.

## GitHub Copilot Prompt

**Original Prompt Used to Create This Project:**

```
Create a Python module named `utils.py` that contains utility functions for real-world tasks like string manipulation and date handling. 

Include at least these functions:
1. format_date(date_obj: datetime, fmt: str = "%Y-%m-%d") -> str
   - Formats a datetime object into a string.
2. capitalize_words(text: str) -> str
   - Capitalizes the first letter of every word in a string.
3. calculate_age(birthdate: str, fmt: str = "%Y-%m-%d") -> int
   - Calculates age from a birthdate string.

For the module and all functions:
- Write **complete Python docstrings**.
- Include: purpose, parameters with types, return values with types, and example usage.

Also generate a **README.md** for this module that includes:
- Module Overview: what it does and why it is useful.
- Setup / Requirements: Python version and dependencies.
- Usage Examples: how to import and use each function.
- Key Functions: list all functions with brief explanations and example usage.
- Written in plain English, professional, and beginner-friendly style.

Additionally, create a comprehensive test file `test_utils.py` that includes:
- Unit tests for all utility functions
- Edge case testing (empty strings, invalid inputs, boundary conditions)
- Error handling validation
- Clear test output with pass/fail indicators
- Make the test file executable and include proper test documentation

Output the complete code for:
1. `utils.py` - Main utility module with full docstrings
2. `test_utils.py` - Comprehensive test suite
3. `README.md` - Complete documentation and usage guide
```

## Module Overview

The `utils.py` module contains a collection of utility functions designed to handle common programming challenges that developers encounter regularly. Whether you need to format dates for user display, capitalize text properly, calculate someone's age, or clean up messy strings, this module provides reliable, tested solutions.

**Why use this module?**
- **Time-saving**: Pre-built functions for common tasks
- **Reliable**: Well-tested implementations with proper error handling
- **Documented**: Complete docstrings with examples for every function
- **Beginner-friendly**: Clear, readable code with comprehensive examples
- **Professional**: Follows Python best practices and coding standards

## Setup / Requirements

### Python Version
- **Required**: Python 3.6 or higher
- **Recommended**: Python 3.8 or higher for best performance

### Dependencies
This module uses only Python's standard library, so no additional packages need to be installed:
- `datetime` - for date/time operations
- `typing` - for type hints (Python 3.6+)
- `re` - for regular expressions (used in whitespace cleaning)

### Installation
1. Download the `utils.py` file
2. Place it in your project directory or Python path
3. Import and start using the functions

```bash
# No pip install required - uses only standard library!
```

## Usage Examples

### Basic Import
```python
# Import the entire module
import utils

# Or import specific functions
from utils import format_date, capitalize_words, calculate_age
```

### Quick Start Example
```python
from datetime import datetime
from utils import format_date, capitalize_words, calculate_age

# Format a date
today = datetime.now()
formatted = format_date(today, "%B %d, %Y")
print(f"Today is: {formatted}")
# Output: Today is: October 11, 2025

# Capitalize text
name = capitalize_words("john doe smith")
print(f"Name: {name}")
# Output: Name: John Doe Smith

# Calculate age
age = calculate_age("1990-05-15")
print(f"Age: {age} years old")
# Output: Age: 35 years old
```

## Key Functions

### 1. `format_date(date_obj, fmt="%Y-%m-%d")`
**Purpose**: Convert datetime objects into formatted strings for display or storage.

**Parameters**:
- `date_obj` (datetime): The datetime object to format
- `fmt` (str, optional): Format string (default: "%Y-%m-%d")

**Returns**: `str` - Formatted date string

**Example Usage**:
```python
from datetime import datetime
from utils import format_date

# Create a datetime object
meeting_time = datetime(2025, 12, 25, 14, 30, 0)

# Different format examples
iso_format = format_date(meeting_time)
# Result: "2025-12-25"

readable_format = format_date(meeting_time, "%B %d, %Y at %I:%M %p")
# Result: "December 25, 2025 at 02:30 PM"

short_format = format_date(meeting_time, "%m/%d/%y")
# Result: "12/25/25"
```

### 2. `capitalize_words(text)`
**Purpose**: Properly capitalize the first letter of every word in a string.

**Parameters**:
- `text` (str): The input string to capitalize

**Returns**: `str` - String with each word capitalized

**Example Usage**:
```python
from utils import capitalize_words

# Basic examples
title = capitalize_words("the great gatsby")
# Result: "The Great Gatsby"

name = capitalize_words("mary jane watson")
# Result: "Mary Jane Watson"

# Works with mixed case
messy_text = capitalize_words("hELLo WoRLD")
# Result: "Hello World"

# Handles multiple spaces
spaced_text = capitalize_words("first   second    third")
# Result: "First   Second    Third"
```

### 3. `calculate_age(birthdate, fmt="%Y-%m-%d")`
**Purpose**: Calculate a person's current age in years from their birthdate.

**Parameters**:
- `birthdate` (str): Birthdate as a string
- `fmt` (str, optional): Format of the birthdate string (default: "%Y-%m-%d")

**Returns**: `int` - Age in complete years

**Example Usage**:
```python
from utils import calculate_age

# Standard ISO format
age1 = calculate_age("1990-03-15")
# Result: 35 (assuming current date is 2025-10-11)

# American format
age2 = calculate_age("03/15/1990", "%m/%d/%Y")
# Result: 35

# European format
age3 = calculate_age("15-03-1990", "%d-%m-%Y")
# Result: 35

# Birthday hasn't happened this year yet
age4 = calculate_age("2000-12-25")
# Result: 24 (birthday is still 2+ months away)
```

### 4. `clean_whitespace(text)`
**Purpose**: Remove extra whitespace and normalize spacing in strings.

**Parameters**:
- `text` (str): The input string to clean

**Returns**: `str` - Cleaned string with normalized whitespace

**Example Usage**:
```python
from utils import clean_whitespace

# Remove extra spaces
cleaned1 = clean_whitespace("  hello    world  ")
# Result: "hello world"

# Handle newlines and tabs
messy_text = "line1\n\n\n\tline2   \n  line3"
cleaned2 = clean_whitespace(messy_text)
# Result: "line1 line2 line3"

# Clean user input
user_input = "   John    Doe   "
cleaned3 = clean_whitespace(user_input)
# Result: "John Doe"
```

### 5. `truncate_string(text, max_length, suffix="...")`
**Purpose**: Shorten strings to fit within length limits with optional suffix.

**Parameters**:
- `text` (str): The input string to potentially truncate
- `max_length` (int): Maximum allowed length (including suffix)
- `suffix` (str, optional): String to append when truncated (default: "...")

**Returns**: `str` - Original or truncated string

**Example Usage**:
```python
from utils import truncate_string

# Basic truncation
short_desc = truncate_string("This is a very long description", 20)
# Result: "This is a very lo..."

# Custom suffix
preview = truncate_string("Long article content here", 15, " (more)")
# Result: "Long art (more)"

# No truncation needed
short_text = truncate_string("Short", 20)
# Result: "Short"

# Perfect for UI previews
title = "Understanding Machine Learning Fundamentals"
card_title = truncate_string(title, 25)
# Result: "Understanding Machine..."
```

## Error Handling

All functions include proper error handling:

- **`format_date`**: Raises `AttributeError` for invalid datetime objects, `ValueError` for invalid format strings
- **`calculate_age`**: Raises `ValueError` for invalid date strings or formats, `TypeError` for non-string input
- **`truncate_string`**: Raises `ValueError` if max_length is shorter than the suffix
- **String functions**: Generally handle empty strings gracefully

## Best Practices

1. **Always handle exceptions** when using date-related functions with user input
2. **Validate input** before calling functions, especially for user-provided data
3. **Use type hints** in your own code when working with these functions
4. **Test edge cases** like empty strings, invalid dates, and boundary conditions

## Example Project Integration

```python
# example_usage.py
from datetime import datetime
from utils import format_date, capitalize_words, calculate_age, clean_whitespace

def process_user_profile(name, birthdate, bio):
    """Process user profile data with utility functions."""
    # Clean and format the name
    clean_name = capitalize_words(clean_whitespace(name))
    
    # Calculate age
    try:
        age = calculate_age(birthdate)
    except ValueError:
        age = "Unknown"
    
    # Format current date for display
    today = format_date(datetime.now(), "%B %d, %Y")
    
    # Clean biography
    clean_bio = clean_whitespace(bio)
    
    return {
        "name": clean_name,
        "age": age,
        "bio": clean_bio,
        "processed_on": today
    }

# Example usage
result = process_user_profile(
    "  john   doe  ",
    "1990-05-15",
    "  Software developer   with   passion for   Python  "
)
print(result)
# Output: {
#     'name': 'John Doe',
#     'age': 35,
#     'bio': 'Software developer with passion for Python',
#     'processed_on': 'October 11, 2025'
# }
```

## Testing

The module includes a comprehensive test suite (`test_utils.py`) that validates all functions with various scenarios, edge cases, and error conditions.

### Running Tests

```bash
# Run the complete test suite
python3 test_utils.py

# Make executable and run (optional)
chmod +x test_utils.py
./test_utils.py
```

### Test Coverage

The test suite includes:
- **Function Tests**: All 5 utility functions thoroughly tested
- **Edge Cases**: Empty strings, invalid inputs, boundary conditions
- **Error Handling**: Validates proper exception handling
- **Integration Tests**: Real-world scenarios using multiple functions
- **Format Validation**: Different date formats and text cases

### Expected Output
```
🚀 Starting comprehensive test suite for utils.py module
...
🎉 ALL TESTS PASSED! The utils module is working perfectly!
```

## File Structure

```
project/
├── utils.py          # Main utility module
├── test_utils.py     # Comprehensive test suite
└── README.md         # This documentation
```

## Contributing

This module is designed to be simple and focused. If you'd like to add more utility functions, ensure they:
- Include complete docstrings with examples
- Handle errors gracefully
- Follow the existing code style
- Use only standard library dependencies
- Are genuinely useful for common programming tasks
- **Add corresponding tests** to `test_utils.py`

### Development Workflow
1. Add your function to `utils.py` with complete docstrings
2. Add comprehensive tests to `test_utils.py`
3. Run `python3 test_utils.py` to verify everything works
4. Update this README with documentation for new functions

---

**Version**: 1.0.0  
**Author**: GitHub Copilot  
**Date**: October 11, 2025  
**License**: Open source - use freely in your projects

## Quick Verification

To verify the module is working correctly on your system:

```bash
# Quick test - should output formatted date
python3 -c "import utils; from datetime import datetime; print(utils.format_date(datetime.now()))"

# Run full test suite
python3 test_utils.py
```