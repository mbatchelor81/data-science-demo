---
trigger: always_on
---

# Python Virtual Environment Rules

## Overview
This project uses a Python virtual environment located in the `.venv/` directory. **This is the ONLY virtual environment that should be used for this project.**

## Mandatory Rules

### 1. **Always Activate the Virtual Environment**
Before starting any work on this project, you **MUST** activate the virtual environment:

```bash
source .venv/bin/activate
```

### 2. **Verify Environment Activation**
After activation, verify you're in the correct environment:

```bash
# Check that your prompt shows (.venv)
# Example: (.venv) user@machine:~/project$

# Verify Python path points to .venv
which python
# Should output: /path/to/project/.venv/bin/python

# Verify pip path points to .venv
which pip
# Should output: /path/to/project/.venv/bin/pip
```

### 3. **Never Use Global Python**
- **DO NOT** run Python commands without activating the virtual environment
- **DO NOT** install packages globally using `pip install` outside the venv
- **DO NOT** use system Python or any other Python installation