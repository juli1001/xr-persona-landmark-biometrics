import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from .features import select_feature_columns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to a CSV (use data/sample/landmarks_dummy.csv for demo)")
    ap.add_argument("--label-col", default="user", help="Label column")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)

    X = select_feature_columns(df)
    y = df[args.label_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    main()
