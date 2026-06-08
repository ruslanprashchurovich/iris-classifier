# Iris Classification (Simple ML Project)

A minimal machine learning project that trains a scikit-learn random forest classifier on the classic Iris dataset.

## 📦 What’s Included

- `src/train.py`: trains a model and prints evaluation metrics
- `src/predict.py`: loads the trained model and makes predictions
- `src/model.py`: small helper module for training/evaluation and persistence
- `requirements.txt`: dependencies needed to run the project
- `.gitignore`: ignores environment artifacts and common Python build files

## 🚀 Quick Start

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python -m src.train
python -m src.predict --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2

# Run REST API
python -m uvicorn src.api:app --reload --port 8000

# Example API request
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

## 🐳 Docker

### Build & Run with Docker

```bash
# Build the image
docker build -t iris-classifier .

# Run a container (execute training or tests)
docker run iris-classifier python -m src.train
docker run iris-classifier pytest -q

# Run API inside container
docker run -p 8000:8000 iris-classifier
```

### Docker Compose

For convenience, use `docker-compose.yml` to run the API with hot-reload:

```bash
docker-compose up
# API will be available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

## 🧠 What It Does

1. Loads the Iris dataset from `sklearn.datasets`.
2. Splits into train/test sets.
3. Trains a RandomForestClassifier.
4. Saves the model to `model.joblib`.
5. Loads the model and predicts labels from command-line inputs.

---

## 🧪 Run Tests

This project includes a small unit test suite using `pytest`.

```bash
pip install -r requirements.txt
pytest -q
```

## 📓 Notebook Demo

A demo notebook is available at `notebooks/demo.ipynb`. It trains the model, saves it, and shows sample predictions.

## 🛠️ Continuous Integration (GitHub Actions)

A GitHub Actions workflow runs `pytest` on every push and pull request to `main`/`master`. The workflow is defined in `.github/workflows/ci.yml`.

---

Feel free to extend this project by adding dataset versioning, model tracking, a small web API, or experiment logging.
