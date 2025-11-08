# Onboarding Guide

## Welcome to Weather API Wrapper Project!

This guide will help you set up your development environment and start contributing to the project.

### Prerequisites

- Python 3.8 or higher
- Git
- Code editor (VS Code recommended)
- Weather API key (from Open-Meteo or similar service)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/github-copilot-hero-mode.git
cd github-copilot-hero-mode
```

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment:

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file or set environment variables:

```bash
export WEATHER_API_KEY=your_api_key_here
```

**Note:** Never commit your `.env` file or API keys to version control!

### Step 5: Verify Installation

Run the test suite to ensure everything is set up correctly:

```bash
pytest --maxfail=1 --disable-warnings
```

### Step 6: Run Tests with Coverage

Check code coverage:

```bash
pytest --cov=src --cov-report=html --cov-report=term
```

Open `htmlcov/index.html` to view detailed coverage report.

### Step 7: Explore the Codebase

**Project Structure:**
```
src/
├── api_client.py       # API communication logic
├── cache_manager.py    # Caching mechanism
└── weather_service.py  # Main service orchestration

tests/
├── test_cache_manager.py    # Cache tests
└── test_weather_service.py  # Service tests
```

### Step 8: Run CodeQL Security Scan

If you have GitHub CLI installed:

```bash
# Install CodeQL CLI (one-time setup)
# Follow: https://github.com/github/codeql-action

# Run analysis
codeql database create codeql-db --language=python
codeql database analyze codeql-db --format=sarif-latest --output=results.sarif
```

Or push to GitHub and let the workflow run automatically.

### Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

3. **Run tests locally:**
   ```bash
   pytest --cov=src
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

5. **Push and create a Pull Request:**
   ```bash
   git push origin feature/your-feature-name
   ```

### Coding Standards

- Follow PEP 8 style guide
- Write docstrings for all public methods
- Maintain >80% test coverage
- Add type hints where appropriate
- Keep functions small and focused

### Testing Guidelines

- Write tests before or alongside code (TDD)
- Test happy paths and edge cases
- Mock external dependencies
- Use descriptive test names
- Aim for 100% coverage of critical paths

### Security Best Practices

- Never hard-code secrets or API keys
- Use environment variables for configuration
- Validate all user inputs
- Handle errors gracefully
- Keep dependencies up to date

### Common Issues

**Issue:** Import errors when running tests
**Solution:** Ensure you're in the virtual environment and all dependencies are installed

**Issue:** API calls failing
**Solution:** Verify your `WEATHER_API_KEY` environment variable is set correctly

**Issue:** Tests failing
**Solution:** Check Python version (3.8+) and ensure all dependencies match requirements.txt

### Getting Help

- Read the [Design Document](DESIGN.md) for architecture details
- Check existing tests for examples
- Review the [README](README.md) for quick reference
- Open an issue on GitHub for bugs or questions

### Next Steps

1. Review the codebase and understand the architecture
2. Run the test suite and explore test coverage
3. Try making a small improvement or fix
4. Read the Design Document for deeper understanding
5. Start contributing!

### Useful Commands

```bash
# Run specific test file
pytest tests/test_cache_manager.py

# Run tests with verbose output
pytest -v

# Run tests and show print statements
pytest -s

# Run tests in parallel (faster)
pytest -n auto

# Check code style
flake8 src/ tests/

# Format code
black src/ tests/
```

### Resources

- [Python Testing with pytest](https://docs.pytest.org/)
- [GitHub CodeQL Documentation](https://codeql.github.com/docs/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

**Happy Coding! 🚀**

If you have questions, don't hesitate to ask the team or open a discussion on GitHub.
