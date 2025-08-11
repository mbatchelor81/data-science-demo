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

### 4. **Package Management Rules**

#### Adding New Dependencies
When you need to add a new import to your code:

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Install the new package
pip install package_name

# 3. Update requirements.txt immediately
pip freeze > requirements.txt

# 4. Reinstall from requirements.txt to verify
pip install -r requirements.txt
```

**CRITICAL**: Never add imports to your code without first installing the package and updating `requirements.txt`.

#### Installing from requirements.txt
```bash
# CORRECT: Install all project dependencies
source .venv/bin/activate
pip install -r requirements.txt
```


### 5. **Development Workflow**

#### Starting Work Session
```bash
# 1. Navigate to project directory
cd /path/to/data-science-demo

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Verify activation (optional but recommended)
which python

# 4. Start your work (Jupyter, Python scripts, etc.)
```

#### Ending Work Session
```bash
# Deactivate when done (optional - closing terminal also works)
deactivate
```

## Important Notes
⚠️ **CRITICAL**: Never commit the `.venv/` directory to version control. It should be in `.gitignore`.
⚠️ **CRITICAL**: Always use `pip freeze > requirements.txt` after installing new packages to keep dependencies up to date.
⚠️ **CRITICAL**: If working in a team, ensure everyone uses the same Python version and installs from the same `requirements.txt`.

## Verification Checklist

Before starting work, ensure:
- [ ] Virtual environment is activated (prompt shows `.venv`)
- [ ] `which python` points to `.venv/bin/python`
- [ ] `which pip` points to `.venv/bin/pip`
- [ ] All required packages are installed (`pip install -r requirements.txt`)

## Team Guidelines

1. **New team members** must create and activate the virtual environment before any work
2. **Before pushing code**, ensure `requirements.txt` is updated with any new dependencies
3. **Before pulling changes**, run `pip install -r requirements.txt` to get new dependencies
4. **Never share** the `.venv/` directory - each developer should have their own

---

**Remember: The `.venv/` directory is the ONLY virtual environment for this project. No exceptions.**
