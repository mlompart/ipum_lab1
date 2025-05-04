import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = "model.joblib"


def load_data():
    """Loads the Iris dataset."""
    iris = load_iris()
    return iris.data, iris.target, iris.target_names


def train_model(X, y):
    """Trains a simple Logistic Regression model."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    print(f"Model Accuracy: {accuracy_score(y_test, model.predict(X_test)):.2f}")
    return model


def save_model(model, filepath):
    """Saves the trained model to a file."""
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")


if __name__ == "__main__":
    X, y, _ = load_data()
    trained_model = train_model(X, y)
    save_model(trained_model, MODEL_PATH)
