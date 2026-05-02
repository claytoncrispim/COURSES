# Django Learning Notes

## Commands We Are Learning

### Migrate command

Command: ```
python manage.py migrate```

What it does:
Applies pending migrations to the database and creates/updates tables to match installed apps.

When to run it:
- Right after creating a new Django project
- After pulling changes that include new migrations
- After installing apps that ship with migrations

---

### Create superuser command

Command: ```
python manage.py createsuperuser```

What it does:
Creates an admin user account with full access to the Django admin panel at `/admin/`.
Prompts for a username, email, and password interactively.

When to run it:
- Once after running `migrate` on a new project
- When you need a new admin account to access the Django admin interface

#### ⚠️ Password validation — never bypass in production

During `createsuperuser`, Django runs a set of built-in password validators before accepting the password.
You can bypass them by typing `y` when prompted with *"This password … bypass password validation and create the user anyway?"*.

**Only do this locally for development convenience. Never bypass validation in production.**

Django's built-in password validators (`AUTH_PASSWORD_VALIDATORS` in `settings.py`) and why they matter:

| Validator | What it checks | Why it matters |
|---|---|---|
| `UserAttributeSimilarityValidator` | Password is not too similar to the username, email, or other user fields | Prevents trivially guessable passwords tied to account info |
| `MinimumLengthValidator` | Password meets a minimum character length (default: 8) | Short passwords are brute-forced very quickly |
| `CommonPasswordValidator` | Password is not in a list of ~20,000 commonly used passwords | Blocks the most targeted passwords in credential-stuffing attacks |
| `NumericPasswordValidator` | Password is not entirely numeric | Pure numeric passwords (e.g. `12345678`) are weak regardless of length |

These validators are configured in `smartnotes/settings.py` under `AUTH_PASSWORD_VALIDATORS` and can be customised or extended with third-party validators for stricter rules in production.

---

## Restricting access with login_required

Goal:
Create a new endpoint that renders `authorized.html` and is accessible only to authenticated users.

### 1. Create the protected view

In `home/views.py`:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/admin')
def authorized(request):
	return render(request, 'home/authorized.html')
```

Why:
- `@login_required` checks if the user is authenticated.
- If not authenticated, Django redirects to the login page.

### 2. Add the endpoint URL

In `home/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
	path('authorized/', views.authorized, name='authorized'),
]
```

### 3. Create the template

Create `home/templates/home/authorized.html`:

```html
<h1>Authorized Area</h1>
<p>If you can see this, you are logged in.</p>
```

### 4. Configure redirect in the decorator (class approach)

Use the decorator argument directly in `home/views.py`:

```python
@login_required(login_url='/admin')
```

Behavior:
- Logged-in users can access `/authorized/`.
- Anonymous users are redirected to `/admin` to log in before accessing `/authorized/`.

Why this is useful:
- Fast, readable access control for function-based views.
- Great default for simple protected pages while learning Django.

