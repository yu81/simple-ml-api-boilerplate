import joblib


def load_model():
    return joblib.load("predictions/models/iris_randomforest.joblib")
