from typing import Tuple
from sklego.datasets import load_penguins
import pandas as pd
import numpy as np


def penguins() -> pd.DataFrame:
    return load_penguins(as_frame=True).dropna(subset=["sex"])


def return_X_y(df: pd.DataFrame) -> Tuple[pd.DataFrame, np.array]:
    X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
    y = df["sex"]
    return X, y
