"""FastAPI endpoints for Iris prediction."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException

from .config import settings
from .constants import CLASS_NAMES
from .model import load_model
from .schemas import IrisFeatures, PredictionResponse

MODEL_PATH = Path(settings.model_path)

app = FastAPI(title="Iris Prediction API", version="0.1.0")

_model = None


def get_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise HTTPException(
                status_code=503,
                detail=f"Model not found. Train model first with `python -m src.train` and ensure {MODEL_PATH} exists.",
            )
        _model = load_model(MODEL_PATH)
    return _model


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": str(MODEL_PATH)}


@app.post("/predict", response_model=PredictionResponse)
def predict(features: IrisFeatures):
    model = get_model()
    prediction = int(model.predict(features.to_array())[0])
    return {
        "predicted_label": prediction,
        "predicted_class": CLASS_NAMES[prediction],
    }
