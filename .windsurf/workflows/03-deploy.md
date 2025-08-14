---
description: Deploy them model once training has completed
auto_execution_mode: 3
---

# Model Deployment Process

## 1. Create a Model
- Once training is complete, use the model artifact saved in S3 to create a SageMaker model.
- This model links the trained artifact with a specific inference container (e.g., XGBoost container).

## 2. Configure Endpoint
- Define an endpoint configuration specifying the instance type and count.
- Choose a cost-effective option like `ml.m5.large` for the demo.

## 3. Deploy the Endpoint
- Deploy the model as a real-time endpoint via SageMaker SDK.
- Wait for the endpoint to become `InService`.

## 4. Make Predictions
- Send new data (without labels) to the endpoint and receive predictions instantly.
- For cost savings in a demo, delete the endpoint after testing to avoid hourly charges.
