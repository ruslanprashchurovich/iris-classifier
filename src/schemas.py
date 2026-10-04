"""Pydantic request/response schemas for the Iris API."""

from __future__ import annotations

import numpy as np
from pydantic import BaseModel, Field

from .constants import CLASS_NAMES


class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., ge=0.0, description="Sepal length in cm")
    sepal_width: float = Field(..., ge=0.0, description="Sepal width in cm")
    petal_length: float = Field(..., ge=0.0, description="Petal length in cm")
    petal_width: float = Field(..., ge=0.0, description="Petal width in cm")

    def to_array(self) -> np.ndarray:
        """Return the features as a (1, 4) array in the model's feature order."""
        return np.array(
            [[self.sepal_length, self.sepal_width, self.petal_length, self.petal_width]]
        )


class PredictionResponse(BaseModel):
    predicted_label: int
    predicted_class: str
    class_names: list[str] = CLASS_NAMES
