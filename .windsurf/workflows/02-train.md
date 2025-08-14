---
description: Train a model in Sagemaker through the SDK
auto_execution_mode: 3
---

# Model Training Process

## 1. Prepare Data
- Query the processed dataset in S3 using AWS Athena via `awswrangler`.
- Split the dataset into training and validation sets (e.g., 80/20 split).
- Save these splits as CSV files in S3 under `models/train/` and `models/validation/`.

## 2. Configure SageMaker
- Use the SageMaker Python SDK to set up a training job.
- Choose a built-in algorithm such as XGBoost for simplicity.
- Specify training parameters like `objective`, `eval_metric`, and `num_round`.

## 3. Launch Training
- Provide S3 paths to the training and validation CSV files as input channels.
- Run the training job on a small instance type (e.g., `ml.m5.large`) to control cost.
- Monitor the job progress in the SageMaker Console and view metrics such as accuracy or AUC.
