"""Entry point for training the Iris classifier."""

from __future__ import annotations

import argparse
import pathlib

import pandas as pd
from sklearn.datasets import load_iris

from .config import settings
from .model import train_and_evaluate, save_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train an Iris classifier")
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(settings.model_path),
        help="Where to write the trained model",
    )
    parser.add_argument(
        "--n-estimators",
        type=int,
        default=settings.n_estimators,
        help="Number of trees in the forest",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=settings.test_size,
        help="Proportion of the dataset to use for evaluation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    iris = load_iris(as_frame=True)
    df = iris.frame

    X = df[iris.feature_names].to_numpy()
    y = df["target"].to_numpy()

    model, metrics = train_and_evaluate(
        X, y, test_size=args.test_size,
        random_state=settings.random_state,
        n_estimators=args.n_estimators,
    )

    save_model(model, args.output)

    print("✅ Training complete")
    print(f"Model written to: {args.output}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    if report := metrics.get("classification_report"):
        print("\nClassification report:")
        print(pd.DataFrame(report).transpose())


if __name__ == "__main__":
    main()
