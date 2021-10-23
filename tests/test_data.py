import pandas as pd
import pytest
from src import data


@pytest.fixture
def df():
    return data.penguins()


def test_shape(df: pd.DataFrame):
    assert df.shape == (333, 7)


def test_X_shape(df: pd.DataFrame):
    X, _ = data.return_X_y(df)
    assert X.shape == (333, 4)


def test_y_shape(df: pd.DataFrame):
    _, y = data.return_X_y(df)
    assert y.shape == (333,)
