# Modeling and Results

After extracting the behavioral features, the next step was to evaluate whether these signals were actually useful for distinguishing between users.

At this stage, the goal was not to build a production-ready system, but to test whether landmark-based behavioral features contain enough signal to detect impersonation patterns.

## Train / Test Strategy

I used a 70/30 stratified split to separate training and testing data. The stratification was important because the dataset includes three classes:

- real user  
- fake1  
- fake2  

Maintaining class balance during the split helped avoid biased evaluation.

No heavy hyperparameter tuning was applied at this stage. The focus was on baseline behavior and interpretability rather than squeezing out marginal gains.

---

## Models Evaluated

I tested three supervised classifiers:

**Logistic Regression**  
Used as a simple linear baseline. It helps understand whether the classes are linearly separable in feature space.

**SVM (RBF kernel)**  
Introduced non-linearity to capture more complex boundaries between behavioral patterns.

**Random Forest**  
Used to capture feature interactions and non-linear relationships without strong distributional assumptions.

Random Forest performed best overall in my experiments.

---

## Observations During Training

One thing I noticed early is that some features contributed more consistently than others. In particular:

- Eye-related features (EAR variations)  
- Head pose angles  
- Certain asymmetry measures  

These seemed to play a stronger role in separability.

It was interesting to see that subtle movement-related features often carried more signal than raw geometric positions.

---

## Results Summary

With the current dataset, the Random Forest classifier achieved approximately **84% accuracy** in distinguishing the real user from impersonators.

While this is not perfect, it is significant given:

- The relatively small dataset  
- The simplicity of the models  
- The fact that this is based purely on landmark-derived behavioral signals  

Confusion patterns revealed that:

- Fake1 was sometimes harder to separate from the real user  
- Fake2 showed clearer behavioral differences  

This suggests that impersonation detectability may depend on how closely the impersonator's behavioral patterns resemble the original user.

---

## Interpretation

These results suggest that landmark-based behavioral biometrics have potential for impersonation detection in XR environments.

The system is not relying on static facial identity features. Instead, it focuses on how the avatar moves and behaves over time.

Even small variations in blink dynamics, head motion, or mouth movement patterns appear to introduce measurable separability.

This opens the door to further exploration using temporal modeling or sequence-based methods.

---

## Limitations

- The dataset size is limited  
- Temporal dependencies are not fully modeled  
- The current approach treats frames mostly independently  

This is a first step toward understanding whether behavioral biometrics can provide an additional security layer for XR avatar systems.
