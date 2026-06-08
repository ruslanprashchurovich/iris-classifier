# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Docker and Docker Compose support
- Configuration management via `.env` and `config.py`
- Pre-commit hooks for code quality
- `pyproject.toml` for modern Python packaging
- Documentation in `docs/` directory
- Dependabot configuration for automated dependency updates
- Contributing guidelines

### Changed
- Updated requirements structure

### Fixed
- Test import paths with `conftest.py`

## [0.1.0] - 2026-06-04

### Added
- Initial project structure
- Iris classification model using RandomForestClassifier
- Training script (`src/train.py`)
- Prediction CLI tool (`src/predict.py`)
- FastAPI REST endpoint (`src/api.py`)
- Model utilities (`src/model.py`)
- Unit tests with pytest
- Jupyter notebook demo
- GitHub Actions CI workflow
- Makefile with common commands
- README with quick start guide

### Features
- Train on Iris dataset
- Make predictions via CLI or REST API
- Interactive API documentation
- Model persistence with joblib

---

## Versioning

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

---

For detailed changes between versions, check the [commit history](https://github.com/ruslanprashchurovich/iris-classifier/commits/main).
