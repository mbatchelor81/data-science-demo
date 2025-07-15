---
trigger: manual
---

# Machine Learning Best Practices

## Versions & Libraries
- Python: 3.8+
- Data Processing: pandas 1.3+, numpy 1.20+
- ML: scikit-learn 1.0+
- API: FastAPI 0.68+
- Experiment Tracking: MLflow 1.20+

## Project Structure
```
data-science-demo/
├── data/                  # Raw and processed data
├── models/                # Serialized models
├── notebooks/             # Exploration notebooks
├── src/                   # Source code
├── api/                   # FastAPI application
├── tests/                 # Test files
├── .github/workflows/     # CI/CD pipelines
├── mlflow/                # MLflow artifacts
```

## scikit-learn Best Practices
- Split data: train (70%), validation (15%), test (15%)
- Use Pipelines for preprocessing
- Apply cross-validation for hyperparameter tuning
- Save models with preprocessing steps included

## FastAPI Deployment
- Use Pydantic for data validation
- Implement health checks
- Document with OpenAPI/Swagger
- Containerize with Docker

## Additional libraries and tools to use
- GitHub Actions (Free Tier)
- MLflow Tracking

## Code Review Checklist
- PEP 8 compliant
- Tests included
- Documentation updated
- No sensitive data
- Models validated
