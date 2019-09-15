from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib


def fit(clf, train_data, test_data, test_ratio):
    train_X, test_X, train_y, test_y = train_test_split(
        train_data, test_data, test_size=test_ratio
    )
    return clf.fit(train_X, train_y), test_X, test_y


if __name__ == "__main__":
    data = load_iris()
    model, test_X, test_y = fit(
        RandomForestClassifier(), data["data"], data["target"], 0.8
    )
    joblib.dump(model, "../models/iris_randomforest.joblib")
