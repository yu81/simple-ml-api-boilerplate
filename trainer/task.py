from typing import List

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, f1_score, matthews_corrcoef

import joblib


def fit():
    data = load_iris()
    train_data = data["data"]
    test_data = data["target"]

    train_X, test_X, train_y, test_y = train_test_split(
        train_data, test_data, test_size=0.8
    )
    clf = RandomForestClassifier(n_estimators=10000)
    clf = clf.fit(train_X, train_y)
    joblib.dump(clf, "../models/iris_randomforest.joblib")
    return clf, test_X, test_y


def predict(clf, test_X: List[List[float]], test_y: List[List[float]]):
    predicted_y = clf.predict(test_X)
    return predicted_y


def evaluate(clf, test_y: List[List[float]], predicted_y: List[int]):
    matrix = confusion_matrix(test_y, predicted_y)
    print("confusion matrix: {}".format(matrix.ravel()))

    f1_score_result = f1_score(test_y, predicted_y, average="micro")
    print("F1 score: {}".format(f1_score_result))

    matthwes_c = matthews_corrcoef(test_y, predicted_y)
    print("Matthews correlation coefficient (MCC): {}".format(matthwes_c))


if __name__ == "__main__":
    clf, test_X, test_y = fit()
    predicted_y = predict(clf, test_X, test_y)
    evaluate(clf, test_y, predicted_y)
