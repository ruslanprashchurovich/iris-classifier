"""FastAPI endpoints for Iris prediction."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .model import load_model

MODEL_PATH = Path("model.joblib")

FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
CLASS_NAMES = ["setosa", "versicolor", "virginica"]


class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., ge=0.0, description="Sepal length in cm")
    sepal_width: float = Field(..., ge=0.0, description="Sepal width in cm")
    petal_length: float = Field(..., ge=0.0, description="Petal length in cm")
    petal_width: float = Field(..., ge=0.0, description="Petal width in cm")


class PredictionResponse(BaseModel):
    predicted_label: int
    predicted_class: str
    class_names: list[str] = CLASS_NAMES


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
    arr = np.array(
        [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width,
        ]]
    )
    prediction = int(model.predict(arr)[0])
    return {
        "predicted_label": prediction,
        "predicted_class": CLASS_NAMES[prediction],
    }
