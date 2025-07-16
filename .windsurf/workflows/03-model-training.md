---
description: Describes splitting data, building pipelines, tuning, and logging to produce a reproducible model artifact
---

## Overview
Training translates cleaned, feature‑engineered data into a reproducible algorithm artifact. Follow a disciplined pipeline to avoid data leakage and stale runs.

### Step 1 — Split Data
Partition into train, validation, and test sets (e.g., 70 / 15 / 15 %) with stratification for classification tasks.

### Step 2 — Build a Processing Pipeline
Use `sklearn.pipeline` (or equivalent) to chain scaling, encoding, and the estimator; guarantees identical transforms during inference.

### Step 3 — Establish a Baseline
Fit a simple model (mean predictor, majority class, or logistic regression) to benchmark future gains.

### Step 4 — Tune Hyper‑parameters
Apply cross‑validated grid, random, or Bayesian search; optimize for the primary metric defined in the evaluation plan.

### Step 5 — Log Experiments
Track parameters, metrics, and artifacts with MLflow or Neptune for lineage and comparison.

### Step 6 — Retrain on Full Data
Once the best configuration is chosen, refit on all available training + validation data; persist the model (e.g., `joblib`, ONNX).