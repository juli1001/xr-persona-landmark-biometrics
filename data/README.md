# Data folder (not committed)

This project uses facial landmark coordinates (x_i, y_i, z_i), which are **biometric-like signals**.

For privacy:
- Do **NOT** upload real participant data to GitHub.
- Keep raw CSVs locally in `data/raw/`.
- Use the included dummy file in `data/sample/` for demos.

Expected CSV columns (example):
- `filename` (frame name)
- `user` (anonymized label like `user_a`)
- Landmark columns like `x_0, y_0, z_0, ...`
- Optional derived features: `ear_left, mar, pitch, yaw, roll`, etc.
