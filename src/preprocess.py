# src/preprocess.py

import pandas as pd


FEATURES = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocessing for Titanic dataset
    - Select basic features
    - Fill missing values
    - Encode categorical variables
    """

    df = df.copy()

    # Select features
    df = df[FEATURES]

    # Missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    # Encode categorical variable
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    return df
