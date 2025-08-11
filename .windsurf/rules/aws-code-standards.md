---
trigger: always_on
---

# AWS + Python Standards (Data Science Workflow)

## Environment
- Use **Python 3.11+** in a dedicated virtual environment (`python -m venv .venv`)
- Pin dependency versions in `requirements.txt`; periodically bump `boto3`

## Credentials & Security
- Prefer **IAM roles** (EC2, SageMaker, Lambda) over static keys.
- Scope IAM policies with **least privilege** (S3 read/write, Glue, SageMaker, CloudWatch).  

## Service‑by‑Service Guide
### Amazon S3 — Data Lake
- Store data under logical prefixes: `raw/`, `processed/`, `feature_store/`.
- Use `upload_file` (multipart) for objects > 100 MB.

### AWS Glue — ETL & Catalog
- Run **Crawlers** to auto‑catalog raw data for Athena.
- Write ETL in **Glue PySpark** (`awsglue` lib); keep jobs idempotent & parameterised (`--S3_BUCKET`, `--RUN_DATE`).
- Use **Job Bookmarks** for incremental loads.

### Amazon EMR — Big‑Data Spark
- Launch **transient EMR clusters** or **EMR Serverless** for >100 GB transforms.
- Store scripts in version‑control; tag clusters (`Environment=demo`) for easy teardown.

### Amazon SageMaker — Train & Deploy
- Use **Processing jobs** for heavy Pandas, **Training jobs** for model fitting.
- Enable **managed spot training** & checkpoints to reduce cost.
- Automate experiments with **Pipelines** or **HyperparameterTuner**; monitor in CloudWatch.

### AWS Lambda — Lightweight Tasks
- Limit work to <15 min, <10 GB memory; perfect for validation, notifications.
- Import heavy libs outside the handler to cut cold‑start latency.

### AWS Step Functions — Orchestration
- Chain Glue → SageMaker → Lambda in one state machine.
- Model each ML stage as a `Task`; use retry/back‑off policies instead of bare `try/except`.
- Export execution history to CloudWatch Logs for audit.

## Coding Patterns
- **Client vs Resource:** default to `boto3.client`; use `resource` only for S3/Dynamo convenience.
- **Pagination:** wrap long listings with `get_paginator`.
- **Error handling:** catch `botocore.exceptions.ClientError`, inspect `response['Error']['Code']`.
- **Logging:** use structured JSON logs at INFO; avoid `print`.

## Infrastructure & CI/CD
- Provision via **AWS CDK (Python)** or Terraform; keep IaC in `/infra`.
- Enforce `pre‑commit` hooks (`black`, `flake8`, `bandit`) and tests (`pytest` + `moto` / `localstack`).

## Cost & Cleanup
- Default to **spot instances** where supported.
- Schedule a Step Functions tag‑sweeper (`ResourceTag=demo`) to auto‑delete demo resources.