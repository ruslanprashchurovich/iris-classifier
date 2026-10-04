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

## 🛠️ Continuous Integration (GitHub Actions)

A GitHub Actions workflow runs `pytest` on every push and pull request to `main`/`master`. The workflow is defined in `.github/workflows/ci.yml`.

## 🏋️ Training Options

The model uses `RandomForestClassifier` with a 75/25 train/test split on four features (sepal length/width, petal length/width) and three classes: Setosa (0), Versicolor (1), Virginica (2).

```bash
python -m src.train --n-estimators 100 --test-size 0.25 --output model.joblib
```

- `--n-estimators`: number of trees in the forest (default: 100)
- `--test-size`: train/test split proportion (default: 0.25)
- `--output`: path to save the model (default: `model.joblib`)

## 🌐 API Reference

Interactive docs: `http://localhost:8000/docs`

**GET** `/health` — returns API status and model path:

```json
{ "status": "ok", "model": "model.joblib" }
```

**POST** `/predict` — predicts the class from flower measurements.

Request:

```json
{ "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2 }
```

Response:

```json
{
  "predicted_label": 0,
  "predicted_class": "setosa",
  "class_names": ["setosa", "versicolor", "virginica"]
}
```

Production run:

```bash
python -m uvicorn src.api:app --host 0.0.0.0 --port 8000
```

## ⚙️ Configuration

Configuration can be set via environment variables (see `.env.example`), command-line arguments, or Python code. Example `.env`:

```
MODEL_PATH=model.joblib
API_PORT=8000
N_ESTIMATORS=100
```

## 🩺 Troubleshooting

- **"Model not found. Train model first..."** — run `python -m src.train`.
- **"Address already in use"** — use a different port: `python -m uvicorn src.api:app --port 8001`.
- **`ModuleNotFoundError: No module named 'src'` in tests** — run `pytest` from the project root (`tests/conftest.py` handles the path).

## ⚡ Performance

- Model training time: < 1 second
- Single prediction time: < 1 ms
- API response time: < 10 ms (typical)
- Model file size: ~100 KB

## 🗺️ Future Enhancements

- [ ] MLflow integration for experiment tracking
- [ ] Model versioning and registry
- [ ] Advanced feature engineering
- [ ] Batch prediction endpoint
- [ ] Web UI dashboard
- [ ] Kubernetes deployment configs

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## 🔗 Repository

- GitHub: https://github.com/ruslanprashchurovich/iris-classifier
- Issues: https://github.com/ruslanprashchurovich/iris-classifier/issues

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

Feel free to extend this project by adding dataset versioning, model tracking, a small web API, or experiment logging.
