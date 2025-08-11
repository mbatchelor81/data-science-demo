---
description: AWS Glue ETL Pipeline Development Workflow
auto_execution_mode: 3
---

# AWS Glue ETL Pipeline Development Workflow

This workflow provides a comprehensive approach to building production-ready AWS Glue ETL pipelines for data processing, following AWS best practices and incorporating data quality findings from EDA analysis.

## Prerequisites

1. **Virtual Environment Setup**
   - Ensure `.venv` is activated: `source .venv/bin/activate`
   - Verify Python path: `which python` (should point to `.venv/bin/python`)
   - Install required dependencies: `pip install -r requirements.txt`

2. **AWS Credentials**
   - Ensure AWS credentials are configured (IAM roles preferred)
   - Test S3 and Glue service access
   - Verify permissions for Glue job creation and execution

3. **EDA Analysis Complete**
   - Review EDA findings for data quality issues
   - Identify missing value patterns, outliers, and business rules
   - Document transformation requirements

## Step 1: Create ETL Project Structure

```bash
mkdir -p 03-etl/{glue_jobs,configs,tests,deploy,utils}
```

Establish organized directory structure:
- **`glue_jobs/`** - Main ETL job scripts
- **`configs/`** - Configuration files and parameters
- **`tests/`** - Unit and integration tests
- **`deploy/`** - Deployment automation scripts
- **`utils/`** - Reusable utility libraries

## Step 2: Create Data Quality Framework

Create `03-etl/utils/data_quality.py` with `DataQualityValidator` class including:

### Core Validation Methods:
- **`validate_schema()`** - Schema structure validation
- **`check_completeness()`** - Missing value analysis with configurable thresholds
- **`check_accuracy()`** - Business rule validation (fare ranges, trip distances, datetime logic)
- **`check_consistency()`** - Cross-field validation and relationship checks
- **`check_duplicates()`** - Duplicate record detection and quantification
- **`run_full_validation()`** - Complete validation pipeline with scoring
- **`generate_quality_report()`** - Human-readable quality assessment

### Key Features Based on EDA Findings:
- **Missing Value Thresholds**: 15% threshold (EDA showed 11.37% pattern)
- **Outlier Detection**: Statistical thresholds for fare amounts, trip distances
- **Business Rules**: Pickup before dropoff, reasonable passenger counts
- **Quality Scoring**: Overall data quality score calculation

## Step 3: Create Transformation Library

Create `03-etl/utils/transformations.py` with `TaxiDataTransformer` class including:

### Data Cleansing Methods:
- **`clean_missing_values()`** - Intelligent imputation strategies (mode, median, constant)
- **`remove_duplicates()`** - Deduplication with logging
- **`handle_outliers()`** - Statistical capping based on EDA distributions
- **`standardize_data_types()`** - Consistent type casting and string cleaning

### Feature Engineering Methods:
- **`extract_datetime_features()`** - Hour, day of week, month, year extraction
- **`calculate_trip_metrics()`** - Speed, duration, tip percentage, cost per mile
- **`encode_categorical_variables()`** - Weekend/rush hour indicators, one-hot encoding
- **`create_derived_features()`** - Location popularity, vendor performance, seasonal indicators

### Pipeline Orchestration:
- **`apply_full_transformation()`** - Complete transformation pipeline
- **`get_transformation_summary()`** - Processing statistics and metrics

## Step 4: Create Main Glue ETL Job Script

Create `03-etl/glue_jobs/taxi_data_etl.py` with `TaxiDataETLJob` class including:

### Core ETL Methods:
- **`load_raw_data()`** - S3 data ingestion using Glue DynamicFrames
- **`validate_data_quality()`** - Integrated quality validation
- **`apply_data_cleansing()`** - Data cleaning based on EDA findings
- **`apply_feature_engineering()`** - Feature creation and enhancement
- **`write_processed_data()`** - Partitioned Parquet output to S3
- **`write_feature_store()`** - ML-ready feature store creation
- **`update_data_catalog()`** - Glue catalog integration
- **`log_job_metrics()`** - CloudWatch metrics logging

### AWS Best Practices Implementation:
- **Parameterized Execution**: CLI arguments for flexibility
- **Error Handling**: Comprehensive exception management
- **Structured Logging**: JSON-formatted logs for analysis
- **Job Bookmarks**: Incremental processing support
- **Resource Management**: Proper Spark context handling

## Step 5: Create Job Configuration File

Create `03-etl/configs/job_config.json` with comprehensive configuration:

### Configuration Sections:
- **Job Configuration**: Worker types, retries, timeouts, Glue version
- **Data Sources**: Input/output S3 paths, formats, compression
- **Data Catalog**: Database and table configurations
- **Data Quality Thresholds**: Based on EDA findings (missing values, outliers)
- **Transformation Config**: Missing value strategies, feature engineering settings
- **Processing Parameters**: Spark optimization settings
- **Monitoring**: CloudWatch metrics and SNS notifications
- **Security**: Encryption, IAM roles, VPC configuration
- **Cost Optimization**: Spot instances, auto-scaling, lifecycle policies

### Environment-Specific Settings:
- **Development**: Smaller worker configuration for testing
- **Staging**: Mid-scale configuration for validation
- **Production**: Full-scale configuration with monitoring

## Step 6: Create Deployment Automation Script

Create `03-etl/deploy/deploy_glue_job.py` with `GlueJobDeployer` class including:

### Infrastructure Management:
- **`create_iam_role()`** - IAM role creation with least privilege
- **`upload_job_script()`** - S3 script deployment with versioning
- **`create_glue_database()`** - Data catalog database setup
- **`create_or_update_glue_job()`** - Job creation/updates with environment configs
- **`create_job_trigger()`** - Scheduled trigger setup (daily at 2 AM UTC)
- **`setup_cloudwatch_dashboard()`** - Monitoring dashboard creation

### Deployment Features:
- **Environment Support**: dev/staging/production configurations
- **Blue-Green Deployment**: Safe deployment strategies
- **Health Checks**: Data quality and performance validation
- **Rollback Capability**: Automated rollback on failure

## Step 7: Implement Comprehensive Testing

Create `03-etl/tests/test_transformations.py` with test suites:

### Test Categories:
- **`TestDataQualityValidator`** - Validation framework testing
- **`TestTaxiDataTransformer`** - Transformation logic testing
- **`TestIntegrationScenarios`** - End-to-end pipeline testing

### EDA-Based Test Scenarios:
- **Missing Value Patterns**: 11.37% missing value scenarios
- **Extreme Outliers**: 297k mile trips, $429k fare scenarios
- **Duplicate Handling**: Single duplicate record scenarios
- **Business Rule Validation**: Datetime logic, fare ranges

### Test Execution:
```bash
cd 03-etl && python -m pytest tests/ -v
```

## Step 8: Update Dependencies

Update `requirements.txt` with ETL-specific dependencies:
```
boto3
pandas
pyspark
pytest
awsglue-library
botocore
numpy
matplotlib
seaborn
```

## Step 9: Deploy ETL Pipeline

### Development Deployment:
```bash
cd 03-etl
python deploy/deploy_glue_job.py --environment development
```

### Production Deployment:
```bash
cd 03-etl
python deploy/deploy_glue_job.py --environment production
```

### Test Job Execution:
```bash
cd 03-etl
python deploy/deploy_glue_job.py --environment development --test-only
```

## Step 10: Monitor and Validate Pipeline

### Monitoring Setup:
- **CloudWatch Dashboard**: `TaxiETL-{environment}-Dashboard`
- **Custom Metrics**: Data quality scores, processing times, record counts
- **Log Analysis**: Structured logs in `/aws/glue/jobs/output`
- **SNS Notifications**: Success/failure alerts

### Data Quality Validation:
- **Quality Thresholds**: 90%+ overall quality score
- **Missing Value Limits**: <15% for any column
- **Business Rule Compliance**: <5% violations
- **Duplicate Detection**: <0.1% duplicate records

## Best Practices Checklist

### Code Quality:
- [ ] Virtual environment activated and dependencies installed
- [ ] All imports at top of files
- [ ] Structured logging implemented throughout
- [ ] Comprehensive error handling for all operations
- [ ] Modular, reusable code architecture

### AWS Standards:
- [ ] IAM roles used (preferred over static keys)
- [ ] Proper exception handling for AWS service calls
- [ ] Resource tagging for cost management
- [ ] Encryption at rest and in transit
- [ ] VPC configuration for security

### Data Quality:
- [ ] EDA findings incorporated into validation rules
- [ ] Configurable quality thresholds
- [ ] Comprehensive business rule validation
- [ ] Automated quality reporting
- [ ] Continuous monitoring setup

### Testing:
- [ ] Unit tests for all transformation functions
- [ ] Integration tests with real-world scenarios
- [ ] EDA-based edge case testing
- [ ] Performance benchmarking
- [ ] End-to-end pipeline validation

### Deployment:
- [ ] Environment-specific configurations
- [ ] Automated deployment scripts
- [ ] Blue-green deployment strategy
- [ ] Health checks and rollback capability
- [ ] Infrastructure as code approach

### Monitoring:
- [ ] CloudWatch dashboards configured
- [ ] Custom metrics implemented
- [ ] Alert thresholds set based on SLAs
- [ ] Log aggregation and analysis
- [ ] Performance monitoring enabled

## Success Criteria

### Pipeline Completion:
- [ ] All ETL components deployed successfully
- [ ] Data quality validation passing (>90% score)
- [ ] Feature engineering producing expected outputs
- [ ] Monitoring dashboards operational
- [ ] Test executions successful

### Output Validation:
- [ ] Processed data in S3 with correct partitioning
- [ ] Feature store populated with ML-ready features
- [ ] Glue Data Catalog updated with schemas
- [ ] Quality reports generated and accessible
- [ ] CloudWatch metrics flowing correctly