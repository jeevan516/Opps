"""Refactored functions from 02-refactoring-functions.ipynb."""

import hashlib

import pandas as pd
from pydantic import BaseModel


def train_and_score(model, X_train, y_train, X_test, y_test):
    """Fit `model` and return it with its test accuracy (percentage, 2 decimals)."""
    model.fit(X_train, y_train)
    accuracy = round(model.score(X_test, y_test) * 100, 2)
    return model, accuracy


def get_active_clients(clients: list[tuple[str, str]]) -> list[str]:
    return [name for name, status in clients if status == "active"]


def split_into_first_and_last_name(name: str) -> list[str]:
    return name.split()


def multiply_column_by_10(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    return df.assign(**{"multiplied column": df[column_name] * 10})


def create_micro_brewery(name: str = "Hipster Brew Co.") -> str:
    slug = hashlib.sha1(name.encode()).hexdigest()
    return f"Microbrewery(name='{name}', slug='{slug}')"


class BannerConfig(BaseModel):
    title: str
    subtitle: str
    button_text: str
    color: str
    dismissible: bool


def create_banner(config: BannerConfig) -> dict:
    return config.model_dump()
