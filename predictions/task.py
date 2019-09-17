from .models import loader
from typing import List

clf = loader.load_model()


def score(test_X: List[List[float]]):
    return clf.score(test_X)
