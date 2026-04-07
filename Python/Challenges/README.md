# Challenges

A standalone Python environment for doing coding challenges and exercises — from Python Essential Training and other sources.

## Setup

```bash
# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Register the Jupyter kernel (for VS Code / JupyterLab)
python -m ipykernel install --user \
  --name="python-challenges" \
  --display-name="Python (Challenges)"
```

## Run tests

```bash
pytest
```

## Structure

```
Challenges/
├── venv/                  # isolated virtual environment (not committed)
├── requirements.txt       # project dependencies
├── .gitignore
└── README.md
```
