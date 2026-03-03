# Landmark Extraction and Feature Engineering

After collecting Persona frames, the next step is landmark extraction.

## Landmark Extraction

For each avatar frame, I use **MediaPipe FaceMesh** to extract:

- 468 facial landmarks
- Each landmark has (x, y, z) coordinates

This results in a high-dimensional representation per frame:

468 landmarks × 3 coordinates = 1404 raw values per frame

These coordinates are stored in CSV format with columns such as:

- `x_0, y_0, z_0`
- `x_1, y_1, z_1`
- ...
- `x_467, y_467, z_467`

Each row corresponds to one captured frame.

---

## Why Raw Landmarks Are Not Enough

While raw landmark coordinates contain detailed geometric information, they:

- Are high dimensional
- Are difficult to interpret directly
- May capture static structure rather than behavioral patterns

Because of this, I transform raw coordinates into **engineered behavioral features**.

---

## Engineered Behavioral Features

From the landmark coordinates, I compute features that capture movement and expression patterns, including:

- Eye Aspect Ratio (EAR) – left and right
- Mouth Aspect Ratio (MAR)
- Mouth vertical and horizontal distances
- Inner eyebrow distance
- Head pose angles (pitch, yaw, roll)
- Left-right asymmetry features
- Head motion magnitude

These features reduce dimensionality while preserving behavioral information.

Instead of modeling static facial geometry, the focus is on dynamic patterns such as:

- Blink frequency and intensity
- Mouth movement during speech
- Head rotation behavior
- Subtle asymmetries in motion

---

## Dataset Structure (Public Version)

This public repository does not include real participant data.

The included dummy dataset preserves:

- The same column structure
- The same feature format
- The same pipeline compatibility

Raw participant landmark data remains local.
