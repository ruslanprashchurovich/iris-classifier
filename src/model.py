"""Model helpers for the Iris classification demo."""

from __future__ import annotations

import pathlib
from typing import Any

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def train_and_evaluate(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.25,
    random_state: int = 42,
    **rf_kwargs: Any,
) -> tuple[RandomForestClassifier, dict[str, Any]]:
    """Train a RandomForestClassifier and return the model + evaluation metrics."""

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    model = RandomForestClassifier(random_state=random_state, **rf_kwargs)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "classification_report": classification_report(y_test, y_pred, output_dict=True),
    }
    return model, metrics


def save_model(model: RandomForestClassifier, path: str | pathlib.Path) -> None:
    """Persist the trained model to disk."""

    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str | pathlib.Path) -> RandomForestClassifier:
    """Load a saved model from disk."""

    return joblib.load(path)
