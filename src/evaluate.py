import json
from dataclasses import dataclass
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


@dataclass
class EvalResult:
    model: str
    accuracy: float
    macro_f1: float
    labels: list
    report: dict
    confusion: list  # list-of-lists for JSON


def evaluate(model_name: str, y_true, y_pred, labels: list) -> EvalResult:
    acc = float(accuracy_score(y_true, y_pred))
    macro_f1 = float(f1_score(y_true, y_pred, average="macro"))
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    return EvalResult(
        model=model_name,
        accuracy=acc,
        macro_f1=macro_f1,
        labels=labels,
        report=report,
        confusion=cm.tolist(),
    )


def save_json(result: EvalResult, out_path: str):
    payload = {
        "model": result.model,
        "accuracy": result.accuracy,
        "macro_f1": result.macro_f1,
        "labels": result.labels,
        "classification_report": result.report,
        "confusion_matrix": result.confusion,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
