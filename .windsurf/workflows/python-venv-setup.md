---
description: Setting up local dev environment for python libraries
---

# Python Virtual Environment Setup

## Prerequisites
- Python 3.8+
- pip (latest version)

## Setup Steps

### Verify python versions
- Validate python versions on the machine
- Select specific one that meets requirements

### Create Virtual Environment
```bash
# Create a virtual environment
python -m venv venv
```

### Activate Virtual Environment

**macOS/Linux**:
```bash
source venv/bin/activate
```

**Windows**:
```bash
venv\Scripts\activate
```

### Install Dependencies
```bash
# Update pip
pip install --upgrade pip

# Install from requirements file
pip install -r requirements.txt
```

### Create Requirements File
```bash
# Generate requirements file
pip freeze > requirements.txt
```

## Core ML Dependencies
```
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
fastapi>=0.68.0
uvicorn>=0.15.0
mlflow>=1.20.0
pytest>=6.2.5
```

## Deactivate Environment
```bash
deactivate
```
