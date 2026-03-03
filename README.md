# Detecting XR Persona Impersonation Using Landmark-Based Biometrics

This repo shows a reproducible pipeline for working with **facial landmark coordinates** and **derived biometric features**
to support identity verification / impersonation detection experiments.

## What this project does
- Loads landmark CSVs with columns like `x_0, y_0, z_0, ...`
- Uses derived features (examples: EAR/MAR, head pose angles)
- Trains baseline ML models and reports metrics
- Saves plots for quick review

## Privacy note
Raw landmark coordinates are **biometric-like**. This repo does **not** include real participant data.
Use the included dummy file:
- `data/sample/landmarks_dummy.csv`

## Quickstart
```bash
pip install -r requirements.txt
python -m src.train --csv data/sample/landmarks_dummy.csv
```

## Repo structure
- `src/` reusable scripts (feature selection, training, evaluation)
- `notebooks/` demos and EDA
- `data/` (raw data is local-only, dummy sample included)
- `reports/figures/` saved plots
