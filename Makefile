VENV=.venv
PYTHON=$(VENV)/Scripts/python
PIP=$(VENV)/Scripts/pip

.PHONY: help venv install train predict serve test clean

help:
	@echo "Usage: make <target>"
	@echo "Targets: venv install train predict serve test clean"

venv:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

train:
	$(PYTHON) -m src.train

predict:
	$(PYTHON) -m src.predict --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2

serve:
	$(PYTHON) -m uvicorn src.api:app --reload --port 8000

test:
	$(PYTHON) -m pytest -q

clean:
	if exist $(VENV) rmdir /s /q $(VENV)
	if exist model.joblib del model.joblib
	if exist __pycache__ rmdir /s /q __pycache__
	if exist .pytest_cache rmdir /s /q .pytest_cache
