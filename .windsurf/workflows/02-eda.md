---
description: Exploratory Data Analysis (EDA) workflow for S3-hosted datasets
auto_execution_mode: 3
---

# Exploratory Data Analysis (EDA) Workflow

This workflow provides a comprehensive approach to performing exploratory data analysis on datasets stored in AWS S3, following data science best practices and AWS standards.

## Prerequisites

1. **Virtual Environment Setup**
   - Ensure `.venv` is activated: `source .venv/bin/activate`
   - Verify Python path: `which python` (should point to `.venv/bin/python`)
   - Install required dependencies: `pip install -r requirements.txt`

2. **AWS Credentials**
   - Ensure AWS credentials are configured (IAM roles preferred)
   - Test S3 access to your target bucket

3. **Project Structure**
   - Create `02-eda/` directory for analysis scripts and outputs
   - Create `02-eda/analysis_output/` for visualizations

## Step 1: Environment Verification

```bash
source .venv/bin/activate && which python && pip list | grep -E "(boto3|pandas|matplotlib|seaborn)"
```

Verify that all required packages are installed and virtual environment is active.

## Step 2: Create S3 Data Loader

Create `02-eda/s3_data_loader.py` with the following components:

- **S3DataLoader class** with proper error handling
- **Pagination support** for large buckets using `get_paginator`
- **Structured logging** with INFO level
- **Methods for**:
  - `list_objects()` - List all objects with optional prefix filtering
  - `download_file()` - Download files to local storage
  - `load_csv_from_s3()` - Direct CSV loading into pandas DataFrame
  - `get_bucket_info()` - Bucket statistics and metadata

**Key AWS Best Practices:**
- Use `boto3.client('s3')` for S3 operations
- Implement proper `ClientError` exception handling
- Use pagination for listing operations
- Include structured logging throughout

## Step 3: Test S3 Connection

```bash
cd 02-eda && python -c "from s3_data_loader import S3DataLoader; loader = S3DataLoader('your-bucket-name'); info = loader.get_bucket_info(); print(f'Found {info[\"total_objects\"]} objects, {info[\"total_size_mb\"]} MB')"
```

Verify S3 connectivity and explore bucket contents.

## Step 4: Create EDA Analysis Script

Create `02-eda/explore_data.py` with `TaxiDataAnalyzer` class including:

### Core Analysis Methods:
- **`load_data()`** - Load and combine multiple CSV files from S3
- **`basic_info()`** - Dataset shape, columns, data types, missing values
- **`statistical_summary()`** - Descriptive statistics for numerical/categorical columns
- **`correlation_analysis()`** - Correlation matrix and high correlation identification
- **`generate_visualizations()`** - Comprehensive plotting suite
- **`generate_report()`** - Markdown report generation
- **`run_full_analysis()`** - Complete pipeline execution

### Visualization Suite:
1. **Dataset Overview** - Missing values, data types, dimensions, memory usage
2. **Numerical Distributions** - Histograms for all numerical columns
3. **Correlation Heatmap** - Correlation matrix with masking
4. **Categorical Analysis** - Top categories for categorical variables

## Step 5: Configure Analysis Parameters

Update the analysis script with your specific parameters:

```python
bucket_name = "your-s3-bucket-name"
analyzer = TaxiDataAnalyzer(bucket_name)
```

Ensure output directories use absolute paths:
```python
self.output_dir = Path(__file__).parent / "analysis_output"
report_path = Path(__file__).parent / "analysis_report.md"
```

## Step 6: Execute Full Analysis

// turbo
```bash
cd 02-eda && python explore_data.py
```

This will:
- Load all CSV files from S3 bucket
- Perform comprehensive EDA
- Generate 4 visualization files
- Create detailed markdown report
- Output results in 02-eda/analysis_output

## Step 7: Review Analysis Results

Examine the generated outputs:

1. **`analysis_output/dataset_overview.png`** - Overall dataset characteristics
2. **`analysis_output/numerical_distributions.png`** - Distribution plots
3. **`analysis_output/correlation_heatmap.png`** - Correlation visualization
4. **`analysis_output/categorical_analysis.png`** - Categorical data analysis
5. **`taxi_data_analysis_report.md`** - Comprehensive analysis report

## Step 8: Data Quality Assessment

Review the analysis report for:

### Critical Issues:
- **Missing Values** - Identify patterns and percentages
- **Duplicate Rows** - Count and impact assessment
- **Outliers** - Extreme values in numerical columns
- **Data Types** - Appropriate type assignments

### Statistical Insights:
- **Correlations** - High correlations (|r| > 0.7) indicating multicollinearity
- **Distributions** - Skewness, normality, and unusual patterns
- **Categorical Patterns** - Frequency distributions and rare categories

## Step 9: Generate Recommendations

Based on analysis results, document:

1. **Data Cleaning Steps**:
   - Missing value handling strategies
   - Outlier treatment approaches
   - Duplicate removal procedures

2. **Feature Engineering Opportunities**:
   - Derived variables from datetime columns
   - Categorical encoding strategies
   - Numerical transformations

3. **Modeling Considerations**:
   - Multicollinearity issues
   - Feature selection recommendations
   - Data preprocessing requirements

## Step 10: Documentation and Handoff

Ensure proper documentation:

- **Analysis Report** - Comprehensive markdown documentation
- **Code Documentation** - Well-commented analysis scripts
- **Visualization Catalog** - Clear descriptions of all plots
- **Recommendations Summary** - Actionable next steps

## Best Practices Checklist

### Code Quality:
- [ ] Virtual environment activated and verified
- [ ] All imports at top of files
- [ ] Structured logging implemented
- [ ] Error handling for all S3 operations
- [ ] Modular, reusable code structure

### AWS Standards:
- [ ] IAM roles used (preferred over static keys)
- [ ] Proper exception handling for `ClientError`
- [ ] Pagination for S3 list operations
- [ ] Efficient data loading strategies

### Analysis Quality:
- [ ] Comprehensive statistical summaries
- [ ] Multiple visualization types
- [ ] Data quality assessment
- [ ] Clear recommendations
- [ ] Reproducible analysis pipeline

### Documentation:
- [ ] Detailed markdown report
- [ ] Code comments and docstrings
- [ ] Clear visualization labels
- [ ] Executive summary included