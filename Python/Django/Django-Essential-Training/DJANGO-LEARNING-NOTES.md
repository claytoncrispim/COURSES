# Django Learning Notes
## Foundations (early modules)

---

## Coverage note

This file captures the early Django modules shown in the course outline: starting your Django project and built-in user management (the part before class_03 notes begin).

---

## Topics covered

1. Creating a new Django project
2. The Model View Template pattern in Django
3. Building a minimum working page
4. Creating your first Django template
5. Django admin for visualizing and managing data
6. Migrations: making database changes easy
7. User authentication in two simple steps

---

## 1. Creating a new Django project

Main command sequence:

```bash
django-admin startproject smartnotes
cd smartnotes
python manage.py runserver
```

What this establishes:
- A Django project with core configuration files
- A working local development server
- The baseline folder structure for apps, settings, urls, and templates

Why this matters:
- It creates the foundation used by every later module (models, views, templates, auth, and admin).

### Important distinction: startproject vs startapp

This was a key confusion point and it is very common when starting Django.

Use this to create the full Django project (global config, settings, urls, wsgi/asgi, admin wiring):

    django-admin startproject smartnotes

Use this to create an application inside the project (where core business features usually live):

    python manage.py startapp <app_name>

Example inside this project:

    python manage.py startapp notes

Quick mental model:
- startproject = whole site skeleton
- startapp = one feature/module inside that site

Practical next steps after creating an app:
1. Add the app to INSTALLED_APPS in settings.py
2. Create models/views/templates for that app
3. Register models in admin.py if needed
4. Add app URLs and include them from project urls.py

---

## 2. The Model View Template pattern in Django

Django uses MVT (Model View Template):
- Model: data structure and database behavior
- View: request handling and business logic
- Template: HTML presentation layer

Learning takeaway:
- Keeping responsibilities separate makes the project easier to grow and debug.

---

## 3. Building a minimum working page

Early in the course, the goal is to return a working response from a route before adding complexity.

Typical flow:
- Create a simple view
- Map URL to that view
- Confirm route works in browser

Why this matters:
- It validates URL routing and response cycle before introducing template inheritance and dynamic data.

---

## 4. Creating your first Django template

After confirming a basic route works, the next step is rendering HTML through Django templates.

Key steps:
- Create template file under the app templates folder
- Render it from a view
- Keep presentation logic in template, not in Python view code

Why this matters:
- This is the first step toward reusable front-end patterns that later evolve into base templates and includes.

---

## 5. Django admin for visualizing and managing data

The admin panel gives a quick way to manage project data through UI.

Main points:
- Create a superuser account
- Access `/admin/`
- Register models in admin to create/read/update/delete data visually

Command used:

```bash
python manage.py createsuperuser
```

---

## 6. Migrations: making database changes easy

Core migration command:

Command:

```bash
python manage.py migrate
```

What it does:
- Applies pending migrations to the database
- Creates or updates tables to match installed apps

When to run it:
- Right after creating a new Django project
- After pulling changes that include migrations
- After installing apps that ship migrations

---

## 7. User authentication in two simple steps

Two-step pattern introduced in this phase:
1. Protect a view using authentication checks
2. Redirect unauthenticated users to login

Example implementation uses `login_required` with `login_url='/admin'`.

### Password validation behavior during superuser creation

During `createsuperuser`, Django runs built-in password validators before accepting a password.

Bypassing validation is possible in development, but should never be done in production.

Built-in validators configured under `AUTH_PASSWORD_VALIDATORS` in `smartnotes/settings.py`:

| Validator | What it checks | Why it matters |
|---|---|---|
| `UserAttributeSimilarityValidator` | Password is not too similar to username/email | Reduces easily guessed account-specific passwords |
| `MinimumLengthValidator` | Password meets minimum length (default 8) | Short passwords are brute-force friendly |
| `CommonPasswordValidator` | Password is not in common-password list | Blocks high-frequency credential-stuffing targets |
| `NumericPasswordValidator` | Password is not fully numeric | Prevents weak numeric-only credentials |

---

### Restricting access with login_required

Goal: render `authorized.html` only for authenticated users.

### View

In `home/views.py`:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html')
```

### URL

In `home/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('authorized/', views.authorized, name='authorized'),
]
```

### Template

In `home/templates/home/authorized.html`:

```html
<h1>Authorized Area</h1>
<p>If you can see this, you are logged in.</p>
```

### Behavior summary

- Authenticated users can access `/authorized/`
- Anonymous users are redirected to `/admin`

---

## 8. Summary of what this file demonstrates

- Starting a Django project and validating local server setup
- Understanding Django's MVT architecture at a practical level
- Moving from minimal route responses to template rendering
- Using Django admin and superuser setup for quick data management
- Running migrations to keep schema in sync with model changes
- Applying `login_required` for simple protected endpoints

