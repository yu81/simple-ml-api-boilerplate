from .models import loader
from typing import List

clf = loader.load_model()


def score(test_X: List[List[float]]) -> float:
    return clf.score(test_X)


def predict(test_X: List[List[float]]) -> List[float]:
    return clf.predict(test_X)


def predict_proba(test_X: List[List[float]]) -> List[List[float]]:
    return clf.predict_proba(test_X)
