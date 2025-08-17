---
trigger: always_on
---

# Virtual Environment Activation Rule for Cascade

## Overview
This rule ensures that Python commands are executed within the project's virtual environment by automatically activating it before running Python-related commands.

## Rule Configuration

### Command Pattern
When running Python commands, always activate the virtual environment first:

```bash
source .venv/bin/activate && python your_script.py
```

### Specific Use Cases

1. **Running Python scripts:**
   ```bash
   source .venv/bin/activate && python download_s3_data.py
   ```

2. **Installing packages:**
   ```bash
   source .venv/bin/activate && pip install package_name
   ```

3. **Running pip commands:**
   ```bash
   source .venv/bin/activate && pip freeze > requirements.txt
   ```

4. **Interactive Python sessions:**
   ```bash
   source .venv/bin/activate && python
   ```

## Why This Matters

- **Dependency Isolation**: Ensures packages are installed and used from the project-specific virtual environment
- **Version Control**: Prevents conflicts between different project dependencies
- **Reproducibility**: Guarantees consistent behavior across different environments

## Implementation Notes

- The virtual environment should be located at `.venv/` in the project root
- Always use `source .venv/bin/activate` (not just `activate`) for proper shell sourcing
- The `&&` operator ensures the Python command only runs if activation succeeds
- This pattern works for any Python-related command that needs access to project dependencies

## Alternative Approach
If you prefer to activate once per session:
```bash
source .venv/bin/activate
# Now all subsequent Python commands will use the virtual environment
python script1.py
pip install requests
python script2.py
```

## Verification
To verify the virtual environment is active, check that the prompt shows `(.venv)` or run:
```bash
which python
# Should show: /path/to/project/.venv/bin/python
```
