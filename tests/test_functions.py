import hashlib

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from exercises.functions import (
    BannerConfig,
    create_banner,
    create_micro_brewery,
    get_active_clients,
    multiply_column_by_10,
    split_into_first_and_last_name,
    train_and_score,
)


def test_get_active_clients():
    clients = [("Ann", "active"), ("Bob", "inactive"), ("Cy", "active")]
    assert get_active_clients(clients) == ["Ann", "Cy"]


def test_split_name_is_pure():
    full_name = "Ryan McDermott"
    assert split_into_first_and_last_name(full_name) == ["Ryan", "McDermott"]
    assert split_into_first_and_last_name(full_name) == ["Ryan", "McDermott"]
    assert full_name == "Ryan McDermott"


def test_multiply_column_does_not_mutate_input():
    original = pd.DataFrame({"values": [1, 2, 3]})
    new = multiply_column_by_10(original, "values")
    assert list(original.columns) == ["values"]
    assert new["multiplied column"].tolist() == [10, 20, 30]


def test_micro_brewery_default_name():
    slug = hashlib.sha1(b"Hipster Brew Co.").hexdigest()
    assert create_micro_brewery() == f"Microbrewery(name='Hipster Brew Co.', slug='{slug}')"


def test_create_banner_from_config():
    config = BannerConfig(
        title="Welcome", subtitle="Try our features", button_text="Start", color="blue", dismissible=True
    )
    assert create_banner(config) == {
        "title": "Welcome",
        "subtitle": "Try our features",
        "button_text": "Start",
        "color": "blue",
        "dismissible": True,
    }


def test_train_and_score_returns_fitted_model_and_percentage():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]
    model, accuracy = train_and_score(DecisionTreeClassifier(random_state=0), X, y, X, y)
    assert accuracy == 100.0
    assert model.predict([[3]])[0] == 1
