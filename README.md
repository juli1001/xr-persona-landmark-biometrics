# Detecting XR Persona Impersonation Using Landmark-Based Biometrics

This project started because I noticed something interesting while working with hyper-realistic XR avatars (Persona-style). 

There is a strong assumption that these avatars are secure by design. However, during controlled testing, I observed that under certain conditions, a different person may temporarily control a user’s avatar. That raised a question for me:

Can we detect impersonation using behavioral signals from facial landmarks?

Instead of focusing only on how the avatar looks, I focused on how it moves.

Even if two avatars appear visually similar, people do not blink, speak, or move their head in exactly the same way. These subtle patterns can work as behavioral signatures.

---

## Overview

The goal of this project is to evaluate whether landmark-based behavioral features can distinguish between:

- the real user  
- impersonator 1 (fake1)  
- impersonator 2 (fake2)  

The approach uses facial landmark coordinates and transforms them into interpretable behavioral features, which are then used in standard machine learning models.

---

## Data Collection Protocol

To keep the experiment controlled, I recorded structured interaction sessions including:

- Neutral face
- Smile
- Blink
- Mouth open / close
- Head turns (left / right)
- Reading a short text aloud

Each recording session generated multiple avatar frames.

For every frame, I extracted **468 facial landmarks (x, y, z coordinates)** using MediaPipe FaceMesh.

---

## Feature Engineering

Raw landmarks are high-dimensional and difficult to interpret directly, so I engineered a smaller set of behavioral features, including:

- Eye Aspect Ratio (EAR) – left and right
- Mouth Aspect Ratio (MAR)
- Mouth vertical and horizontal distances
- Inner eyebrow distance
- Head pose angles (pitch, yaw, roll)
- Left-right asymmetry features
- Head motion magnitude

These features are intended to capture behavioral differences rather than static facial geometry.

---

## Models Tested

I evaluated three supervised classifiers:

- Logistic Regression (baseline)
- SVM with RBF kernel
- Random Forest

The dataset was split using a 70/30 stratified train-test setup.

---

## Results

With the current dataset, the Random Forest model achieved approximately **84% accuracy** in distinguishing the real user from impersonators.

One interesting observation is that impersonator 1 was sometimes harder to separate from the real user compared to impersonator 2. This suggests that certain behavioral similarities may reduce separability.

These results are preliminary, but they show that landmark-based behavioral features have potential for impersonation detection in XR environments.

---

## Repository Structure

- `src/` – reusable scripts for feature selection and baseline training
- `notebooks/` – demonstration and exploratory analysis
- `data/` – no real participant data included (public portfolio version)
- `reports/figures/` – plots used for visualization

---

## Privacy Note

This is a public portfolio version of the project.

- No real participant landmark data is included.
- A dummy dataset is provided only to demonstrate the pipeline.
- Raw landmark data remains local.

---

## How to Run (Demo)

```bash
pip install -r requirements.txt
python -m src.train --csv data/sample/landmarks_dummy.csv
