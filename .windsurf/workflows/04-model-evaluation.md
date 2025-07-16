---
description: Explains how to measure, diagnose, and document model performance and robustness on unseen data
---

## Overview
Evaluation quantifies **generalization and business fitness** on unseen data; choose metrics aligned with the problem.

### Step 1 — Select Metrics
Classification → Accuracy, Precision, Recall, F1, ROC‑AUC  
Regression → MAE, RMSE, R²

### Step 2 — Compute Hold‑out Scores
Run the frozen model on the test set exactly once; record metric values and confidence intervals.

### Step 3 — Inspect Error Structure
Draw a confusion matrix or residual plots to spot bias, heteroscedasticity, or systematic failure modes.

### Step 4 — Compare Against Baseline & KPI
Ensure improvement over baseline and that domain‑specific thresholds are met (e.g., recall > 0.9 for fraud).

### Step 5 — Perform Robustness Checks
Validate with k‑fold averages, permutation tests, and adversarial data slices.

### Step 6 — Document & Sign‑off
Log metrics, plots, and rationale in a version‑controlled report; obtain stakeholder approval before deployment.