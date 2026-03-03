import pandas as pd

DERIVED_FEATURES = [
    "ear_left","ear_right","mar","brow_distance",
    "eye_open_left","eye_open_right",
    "mouth_vertical","mouth_horizontal",
    "pitch","yaw","roll"
]

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def select_feature_columns(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in DERIVED_FEATURES if c in df.columns]
    if not cols:
        raise ValueError("No derived feature columns found. Update DERIVED_FEATURES or create features first.")
    return df[cols].copy()
