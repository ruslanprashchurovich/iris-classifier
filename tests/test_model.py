"""Unit tests for the Iris model training and prediction helpers."""

import numpy as np
from sklearn.datasets import load_iris

from src.model import train_and_evaluate, save_model, load_model


def test_train_and_evaluate_smoke(tmp_path):
    iris = load_iris(as_frame=True)
    X = iris.frame[iris.feature_names].to_numpy()
    y = iris.frame["target"].to_numpy()

    model, metrics = train_and_evaluate(X, y, test_size=0.2, random_state=0, n_estimators=10)

    assert "accuracy" in metrics
    assert metrics["accuracy"] > 0.5

    model_path = tmp_path / "model.joblib"
    save_model(model, model_path)

    loaded = load_model(model_path)
    sample = np.atleast_2d(X[0])
    pred = loaded.predict(sample)
    assert pred.shape == (1,)
