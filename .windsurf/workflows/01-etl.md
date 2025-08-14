---
description: Conduct the ETL Process from an S3 bucket
auto_execution_mode: 3
---

# ETL Process

## 1. Extract
- Connect to your AWS S3 bucket where your raw data is stored.
- Read the files (e.g., CSV, JSON) from the `raw/` folder using a Python library like `awswrangler` or `pandas`.
- Ensure you have IAM permissions to list and read these objects.

## 2. Transform
- Clean the data: remove duplicates, fill or drop missing values, fix data types.
- Feature Engineering: Add new columns or features that will help your model.
- Keep transformations simple, such as converting date formats or calculating lengths of text.

## 3. Load
- Save the cleaned dataset back to S3 in the `processed/` folder as Parquet files (efficient for queries).
- Use `awswrangler` to register the processed data in the AWS Glue Data Catalog.
- This makes the data queryable via AWS Athena, so you can preview results directly in AWS Console or Python.
