---
description: Machine Learning Model Training Workflow for Taxi Data
auto_execution_mode: 3
---

# Machine Learning Model Training Workflow for Taxi Data

Build and deploy ML models using the processed taxi data from our ETL pipeline.

## Prerequisites

- ETL pipeline completed with processed data in S3
- Virtual environment activated: `source .venv/bin/activate`
- AWS credentials configured for SageMaker access

## Step 1: Setup Project Structure

```bash
mkdir -p 04-training/{notebooks,models,configs}
```

## Step 2: Load Feature Store Data

Create `04-training/load_features.py`:
- Load processed data from ETL S3 bucket
- Select ML features: trip_distance, pickup_hour, is_weekend, etc.
- Create target variable: fare_amount or trip_duration_minutes

## Step 3: Train Baseline Model

Create `04-training/train_model.py`:
- Split data: 70% train, 15% validation, 15% test
- Train simple linear regression baseline
- Evaluate with RMSE and MAE metrics

## Step 4: Train Advanced Models

Add to `train_model.py`:
- XGBoost model with hyperparameter tuning
- Random Forest for comparison
- Cross-validation with 5 folds

## Step 5: Model Evaluation

Create `04-training/evaluate_model.py`:
- Calculate regression metrics (RMSE, MAE, R²)
- Generate prediction vs actual plots
- Feature importance analysis

## Step 6: Deploy to SageMaker

Create `04-training/deploy_model.py`:
- Register best model in SageMaker Model Registry
- Deploy to real-time endpoint
- Setup batch transform for large-scale inference

// turbo
## Step 7: Run Training Pipeline

```bash
cd 04-training
python load_features.py
python train_model.py
python evaluate_model.py
python deploy_model.py
```

## Success Criteria

- [ ] Baseline model RMSE < $5.00 for fare prediction
- [ ] Advanced model improves baseline by >15%
- [ ] Model deployed to SageMaker endpoint
- [ ] Inference latency < 100ms

## Use Cases

1. **Fare Prediction**: Predict trip cost based on distance, time, location
2. **Duration Prediction**: Estimate trip time for route planning
3. **Demand Forecasting**: Predict taxi demand by location and hour