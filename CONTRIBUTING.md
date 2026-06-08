# Contributing Guide

Thank you for your interest in contributing to Iris Classifier! Here's how you can help.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/ruslanprashchurovich/iris-classifier.git
   cd iris-classifier
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows
   source .venv/bin/activate   # macOS/Linux
   ```
4. **Install dev dependencies**:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

## Development Workflow

### Making Changes

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure tests pass:
   ```bash
   pytest -q
   ```

3. Format your code:
   ```bash
   black .
   isort .
   flake8 .
   ```

4. Commit with descriptive messages:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — A new feature
- `fix:` — A bug fix
- `docs:` — Documentation changes
- `style:` — Code formatting (black, isort, etc.)
- `test:` — Adding or updating tests
- `refactor:` — Code refactoring without behavior change
- `ci:` — CI/CD configuration changes

## Testing

Write tests for new features in `tests/`:

```bash
pytest -q                    # Run all tests
pytest -v                    # Verbose output
pytest --cov                 # With coverage report
pytest tests/test_model.py   # Run specific test file
```

## Pull Request Process

1. Push to your fork
2. Open a Pull Request against `main`
3. Ensure CI/CD passes (GitHub Actions)
4. Request review from maintainers
5. Address any feedback

## Code Style

We use:
- **Black** for formatting
- **isort** for import sorting
- **Flake8** for linting
- **pre-commit** to automate checks

Install and use pre-commit:
```bash
pre-commit install
pre-commit run --all-files
```

## Reporting Issues

- Check if the issue already exists
- Include Python version and OS
- Provide minimal reproducible example
- Add relevant error messages

## Questions?

- Open a GitHub Discussion
- Check existing issues and PRs
- Contact maintainers

---

Happy coding! 🎉
