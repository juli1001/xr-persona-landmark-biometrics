import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def get_X_y(df: pd.DataFrame, feature_cols: list[str], label_col: str):
    if label_col not in df.columns:
        raise ValueError(f"Label column '{label_col}' not found in CSV.")

    missing = [c for c in feature_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing feature columns in CSV: {missing}")

    X = df[feature_cols].copy()
    y = df[label_col].copy()
    return X, y


def split_data(X, y, test_size: float = 0.30, random_state: int = 42):
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )


def fit_scaler(X_train):
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    return X_train_s, scaler


def apply_scaler(X_test, scaler: StandardScaler):
    return scaler.transform(X_test)
