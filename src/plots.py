import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def plot_model_comparison(models, accuracies, macro_f1s, out_path: str): #Bar chart comparing Accuracy and Macro F1 across models.
  
    _ensure_dir(os.path.dirname(out_path))

    x = np.arange(len(models))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar(x - width / 2, accuracies, width, label="Accuracy")
    plt.bar(x + width / 2, macro_f1s, width, label="Macro F1")

    plt.xticks(x, models, rotation=15)
    plt.ylim(0, 1.0)
    plt.ylabel("Score")
    plt.title("Model Comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_confusion_matrix(y_true, y_pred, labels, title: str, out_path: str):
    _ensure_dir(os.path.dirname(out_path))

    disp = ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred,
        display_labels=labels,
        cmap=None  # don't set colors manually
    )
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_feature_importance(feature_names, importances, out_path: str, top_k: int = 10): #Horizontal bar chart of top-k feature importances.
    _ensure_dir(os.path.dirname(out_path))

    feature_names = np.array(feature_names)
    importances = np.array(importances)

    idx = np.argsort(importances)[::-1][:top_k]
    top_feats = feature_names[idx]
    top_imps = importances[idx]

    plt.figure(figsize=(7, 5))
    plt.barh(top_feats[::-1], top_imps[::-1])
    plt.title(f"Top {top_k} Feature Importances (Random Forest)")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_scatter_by_label(df, x_col: str, y_col: str, label_col: str, out_path: str, title: str): #Scatter plot colored by label.
    
    _ensure_dir(os.path.dirname(out_path))

    plt.figure(figsize=(6, 6))
    for label, sub in df.groupby(label_col):
        plt.scatter(sub[x_col], sub[y_col], alpha=0.5, label=str(label))

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_corr_matrix(df, feature_cols, out_path: str, title: str): #Simple correlation heatmap.
    
    _ensure_dir(os.path.dirname(out_path))

    corr = df[feature_cols].corr()

    plt.figure(figsize=(9, 7))
    im = plt.imshow(corr, interpolation="nearest")
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.xticks(range(len(feature_cols)), feature_cols, rotation=90)
    plt.yticks(range(len(feature_cols)), feature_cols)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_boxplots_grid(df, feature_cols, label_col: str, out_path: str, title: str): #Grid of boxplots per feature grouped by label.
    
  
    _ensure_dir(os.path.dirname(out_path))

    n = len(feature_cols)
    cols = 3
    rows = int(np.ceil(n / cols))

    fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
    axes = np.array(axes).reshape(rows, cols)

    labels = sorted(df[label_col].unique().tolist())

    for i, feat in enumerate(feature_cols):
        r, c = divmod(i, cols)
        ax = axes[r, c]

        data = [df[df[label_col] == lab][feat].dropna().values for lab in labels]
        ax.boxplot(data, labels=labels)
        ax.set_title(f"{feat} by {label_col}")
        ax.set_xlabel("")
        ax.set_ylabel(feat)
        ax.grid(True, alpha=0.2)

    # Remove empty axes
    for j in range(n, rows * cols):
        r, c = divmod(j, cols)
        fig.delaxes(axes[r, c])

    plt.suptitle(title, y=1.02)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()
