from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


def get_logreg(seed: int = 42)  #LogisticRegression:
    # Simple, strong baseline for multiclass
    return LogisticRegression(
        max_iter=2000,
        random_state=seed,
        multi_class="auto"
    )


def get_svm_rbf(seed: int = 42) #SVC:
    # probability=True helps later if you want ROC curves
    return SVC(
        kernel="rbf",
        probability=True,
        random_state=seed
    )


def get_random_forest(seed: int = 42) #RandomForestClassifier:
    return RandomForestClassifier(
        n_estimators=300,
        random_state=seed
    )


def get_models(seed: int = 42):
    return {
        "logreg": get_logreg(seed),
        "svm_rbf": get_svm_rbf(seed),
        "random_forest": get_random_forest(seed),
    }
