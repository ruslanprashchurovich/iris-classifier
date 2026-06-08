# Iris Classifier Documentation

## Overview

The Iris Classifier is a lightweight machine learning application for classifying iris flowers using scikit-learn's RandomForest algorithm.

## Architecture

```
src/
├── train.py      # Training entry point
├── predict.py    # CLI prediction tool
├── api.py        # FastAPI REST endpoint
└── model.py      # Model utilities (train, save, load)
```

## Training

The model is trained on the classic Iris dataset with:
- **Algorithm**: RandomForestClassifier
- **Split**: 75% training, 25% testing
- **Features**: Sepal length, sepal width, petal length, petal width
- **Classes**: Setosa (0), Versicolor (1), Virginica (2)

### Training from CLI

```bash
python -m src.train --n-estimators 100 --test-size 0.25 --output model.joblib
```

**Options:**
- `--n-estimators`: Number of trees in the forest (default: 100)
- `--test-size`: Train/test split proportion (default: 0.25)
- `--output`: Path to save the model (default: model.joblib)

## API Reference

### Health Check

**GET** `/health`

Returns API status and model path.

**Response:**
```json
{
  "status": "ok",
  "model": "model.joblib"
}
```

### Prediction Endpoint

**POST** `/predict`

Makes a prediction based on iris flower measurements.

**Request Body:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**
```json
{
  "predicted_label": 0,
  "predicted_class": "setosa",
  "class_names": ["setosa", "versicolor", "virginica"]
}
```

### Running the API

```bash
# Development (with hot-reload)
python -m uvicorn src.api:app --reload --port 8000

# Production
python -m uvicorn src.api:app --host 0.0.0.0 --port 8000
```

**Interactive docs available at:** `http://localhost:8000/docs`

## Docker

### Build Image

```bash
docker build -t iris-classifier .
```

### Run Training in Container

```bash
docker run iris-classifier python -m src.train
```

### Run API in Container

```bash
docker run -p 8000:8000 iris-classifier
```

### Using Docker Compose

```bash
docker-compose up
```

## Testing

Run the test suite:

```bash
pytest -q
pytest -v          # Verbose
pytest --cov       # Coverage report
```

Test file: `tests/test_model.py`

## Configuration

Configuration can be set via:
1. Environment variables (see `.env.example`)
2. Command-line arguments
3. Python code directly

Example `.env` file:
```
MODEL_PATH=model.joblib
API_PORT=8000
N_ESTIMATORS=100
```

## Troubleshooting

### Model Not Found Error

**Error:** "Model not found. Train model first..."

**Solution:**
```bash
python -m src.train
```

### Port Already in Use

**Error:** "Address already in use"

**Solution:**
```bash
# Use a different port
python -m uvicorn src.api:app --port 8001
```

### Import Errors in Tests

**Error:** "ModuleNotFoundError: No module named 'src'"

**Solution:** The project includes `tests/conftest.py` which should handle this. Ensure you run:
```bash
pytest from the project root
```

## Performance

- **Model training time**: < 1 second
- **Single prediction time**: < 1 ms
- **API response time**: < 10 ms (typical)
- **Model file size**: ~100 KB

## Future Enhancements

- [ ] MLflow integration for experiment tracking
- [ ] Model versioning and registry
- [ ] Advanced feature engineering
- [ ] Batch prediction endpoint
- [ ] Web UI dashboard
- [ ] Kubernetes deployment configs

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines.

## Repository

- **GitHub**: https://github.com/ruslanprashchurovich/iris-classifier
- **Issues**: https://github.com/ruslanprashchurovich/iris-classifier/issues

## License

MIT License - see [LICENSE](../LICENSE)
