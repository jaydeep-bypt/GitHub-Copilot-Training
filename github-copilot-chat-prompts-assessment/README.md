# Week 2 Copilot Training Assessment

## Original Function Purpose

The legacy function (`proc_usr_dt`) processes a CSV file containing user data (name, age, city). It reads the file, groups users by city, counts users per city, and collects their ages. The code is messy, uses unclear variable names, and lacks robust error handling.

## Copilot's Role

GitHub Copilot:
- Explained the legacy function step by step in plain English.
- Refactored the function using modern Python practices (async file I/O, clear naming, error handling).
- Provided a CLI/test example for easy verification.
- Created a professional project structure and documentation.

## Key Improvements in the Refactored Version

- **Clear variable and function names** for readability.
- **Async file reading** for better performance (if applicable).
- **Structured error handling** for robustness.
- **Type hints and docstrings** for maintainability.
- **CLI/test example** for direct verification.
- **Consistent formatting and code style**.

---


---

## Using GitHub Copilot CLI

You can use GitHub Copilot CLI to generate, explain, and refactor code directly from your terminal. This complements the Copilot experience in VS Code.

### Installation

1. Install Node.js (if not already installed): https://nodejs.org/
2. Install Copilot CLI:
	```powershell
	npm install -g @githubnext/github-copilot-cli
	```
3. Authenticate with your GitHub account:
	```powershell
	copilot login
	```

### Example Usage in This Project

**Suggest code:**
```powershell
copilot suggest "Write a Python function to process CSV user data"
```

**Explain code:**
```powershell
copilot explain week2_copilot_assessment/legacy_function.py
```

**Refactor code:**
```powershell
copilot generate week2_copilot_assessment/modern_function.py
```

**Get help:**
```powershell
copilot help
```

For more details, see the [Copilot CLI documentation](https://githubnext.com/projects/copilot-cli/).
