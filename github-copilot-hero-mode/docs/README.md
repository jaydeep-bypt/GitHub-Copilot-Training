# Week 8 — Hero Mode: Full Workflow

## Project
Weather API wrapper with caching — demonstrating full SDLC using GitHub Copilot.

### Features
- Fetch current weather data for a city.
- Cache responses for 10 minutes.
- Use environment variable for API key.
- Fully tested and secure.

### Tech Stack
- Python 3.x
- pytest (unit tests)
- CodeQL (security scan)

### Quick Start
1. Clone the repository
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variable:
   ```bash
   export WEATHER_API_KEY=your_api_key_here
   ```
5. Run tests:
   ```bash
   pytest --maxfail=1 --disable-warnings --cov=src
   ```

### Project Structure
```
github-copilot-hero-mode/
├── src/                    # Source code
│   ├── api_client.py       # API communication
│   ├── cache_manager.py    # Caching logic
│   └── weather_service.py  # Main service
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── reports/                # Security reports
└── .github/workflows/      # CI/CD workflows
```

### Testing
Run tests with coverage:
```bash
pytest --cov=src --cov-report=html
```

### Security
This project follows secure coding practices:
- Environment variables for secrets
- Input validation
- Request timeouts
- CodeQL security scanning

### License
MIT License
