# Jupyter Lab Setup — Python Essential Training

## Prerequisites

- Python 3.12+ installed (`python3 --version`)
- Working directory: `Python-Essential-Training/`

---

## 1. Create the virtual environment

```bash
cd Python-Essential-Training
python3 -m venv venv
```

---

## 2. Activate the virtual environment

```bash
source venv/bin/activate
```

> On Windows: `venv\Scripts\activate`

---

## 3. Install Jupyter packages

```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:

```
jupyterlab
notebook
ipykernel
```

---

## 4. Register the kernel (so VS Code and JupyterLab can find it)

```bash
python -m ipykernel install --user \
  --name="python-essential-training" \
  --display-name="Python (Essential Training)"
```

Verify the kernel is registered:

```bash
jupyter kernelspec list
```

---

## 5. Launch JupyterLab

From inside `Python-Essential-Training/`:

```bash
jupyter lab
```

JupyterLab will open in your browser. Navigate to:

```
Ex_Files_Python_EssT/Exercise Files/exercise_files/
```

to find all the `.ipynb` notebook files.

---

## 6. Select the correct kernel in VS Code

When opening a `.ipynb` file in VS Code:

1. Click the kernel selector in the top-right corner of the notebook.
2. Choose **"Python (Essential Training)"** from the list.

---

## Notes on venv isolation

Each sub-project under `Python/` has its own independent venv:

| Project | venv path | Purpose |
|---|---|---|
| `Python-Essential-Training/` | `venv/` | Jupyter only |
| `python-chatgpt-mentoring/` | `venv/` | FastAPI, pytest, pydantic |

Do **not** install Jupyter into `python-chatgpt-mentoring/venv`, and do **not** install FastAPI packages into `Python-Essential-Training/venv`. Keep them isolated to avoid conflicts.

---

## Quick reference commands

```bash
# Activate
source venv/bin/activate

# Check Jupyter version
jupyter lab --version

# List registered kernels
jupyter kernelspec list

# Start JupyterLab
jupyter lab

# Deactivate when done
deactivate
```
