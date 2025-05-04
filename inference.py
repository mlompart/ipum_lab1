import joblib
import numpy as np
from sklearn.datasets import load_iris

MODEL_PATH = "model.joblib"

# Load target names when the module is imported
TARGET_NAMES = load_iris().target_names


def load_model(filepath=MODEL_PATH):
    """Loads the trained model from a file."""
    return joblib.load(filepath)


def predict(model, input_data: list):
    """Uses the model to make predictions."""
    prediction_numeric = model.predict(np.array(input_data).reshape(1, -1))
    prediction_label = TARGET_NAMES[prediction_numeric[0]]
    return prediction_label
