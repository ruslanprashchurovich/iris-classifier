"""Load a trained model and make a prediction from command-line features."""

from __future__ import annotations

import argparse
import pathlib

import numpy as np

from .model import load_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Predict using a trained Iris model")
    parser.add_argument(
        "--model",
        type=pathlib.Path,
        default=pathlib.Path("model.joblib"),
        help="Path to the trained model file",
    )
    parser.add_argument(
        "--sepal-length",
        type=float,
        required=True,
        help="Sepal length in cm",
    )
    parser.add_argument(
        "--sepal-width",
        type=float,
        required=True,
        help="Sepal width in cm",
    )
    parser.add_argument(
        "--petal-length",
        type=float,
        required=True,
        help="Petal length in cm",
    )
    parser.add_argument(
        "--petal-width",
        type=float,
        required=True,
        help="Petal width in cm",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    model = load_model(args.model)

    features = np.array(
        [[args.sepal_length, args.sepal_width, args.petal_length, args.petal_width]]
    )

    prediction = model.predict(features)[0]

    print("✅ Prediction complete")
    print(f"Predicted class label: {int(prediction)}")


if __name__ == "__main__":
    main()
