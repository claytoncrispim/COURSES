# Django — New Project Cheatsheet

## 1. Create & activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
pip install --upgrade pip
pip install django
```

---

## 2. Start a new project

```bash
django-admin startproject <project_name> .
```

> The trailing `.` places `manage.py` in the current directory instead of creating an extra subdirectory.

**This course:**
```bash
django-admin startproject smartnotes .
```

---

## 3. Create an app inside the project

```bash
python manage.py startapp <app_name>
```

> Do **not** pass `.` here — Django uses the current directory name as the app name, which will fail if it contains hyphens.

**Register the app** in `<project_name>/settings.py`:
```python
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```

---

## 4. Run the development server

```bash
python manage.py runserver
```

Accessible at <http://127.0.0.1:8000/> by default.

---

## 5. Common manage.py commands

| Command | Purpose |
|---|---|
| `python manage.py check` | Validate project configuration |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Generate migration files from model changes |
| `python manage.py createsuperuser` | Create an admin user |
| `python manage.py shell` | Open Django interactive shell |
| `python manage.py collectstatic` | Gather static files for deployment |

---

## 6. Typical project layout after setup

```
manage.py
<project_name>/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
<app_name>/
    migrations/
    templates/
        <app_name>/
    __init__.py
    admin.py
    apps.py
    models.py
    urls.py
    views.py
```
