# Django Learning Notes - class_05
## Module 05 - Building Robust Front-Ends in Django

---

## Module 05 chapters covered so far

1. Static files in Django
2. An HTML skeleton: how to set up a base structure to every Django template
3. It's time to add some style

---

## 1. Static files in Django

### Main concept

Static files are assets that are not generated dynamically by Python code, such as CSS files, JavaScript files, and images. Django needs to know where those files live so templates can load them correctly.

### What I changed in code

- In `smartnotes/settings.py`, I configured `STATIC_URL = 'static/'`.
- In `smartnotes/settings.py`, I added `STATICFILES_DIRS = [BASE_DIR / 'static/']` so Django can look inside the project's shared `static/` folder.
- I created the folder structure `static/css/` and added `static/css/style.css`.

### Why this matters

Without static file configuration, Django templates would not be able to load shared CSS, JavaScript, or images. This is the foundation for styling the project consistently across pages.

### Beginner note

- `STATIC_URL` is the URL prefix used in templates.
- `STATICFILES_DIRS` tells Django where to find your local static assets during development.
- The actual file path can be different from the URL path.

Example:

- File on disk: `static/css/style.css`
- Template reference: `{% static 'css/style.css' %}`

---

## 2. Base template for shared page structure

### Main concept

Instead of repeating the same HTML skeleton in every page, Django lets you create one base template and have other templates extend it. This keeps layout code in one place and makes updates much easier.

### What I changed in code

- I created `static/templates/base.html` as the shared layout template.
- In `smartnotes/settings.py`, I added `BASE_DIR / 'static/templates'` to `TEMPLATES['DIRS']` so Django can find `base.html`.
- The base template includes:
	- `{% load static %}`
	- the shared `<html>`, `<head>`, and `<body>` structure
	- a Bootstrap CDN link
	- a `{% block content %}` section for child templates

### Why this matters

This gives every page a consistent structure and avoids duplicating boilerplate HTML. When you want to change the layout later, you only need to update one file.

### Beginner note

The child template uses:

```html
{% extends "base.html" %}
```

That means: "Use the HTML structure from `base.html`, and only replace the named block sections I define here."

---

## 3. Styling templates

### Main concept

Once the static and template structure is ready, styling becomes much easier. In this stage, the project uses two styling approaches:

- Bootstrap utility classes from a CDN
- Your own CSS rules in `static/css/style.css`

### What I changed in code

- In `static/templates/base.html`, I linked Bootstrap from a CDN.
- In `static/css/style.css`, I added custom classes such as:
	- `.note-li`
	- `.note-detail`
	- `.note-popular`
- In templates like `notes/templates/notes/notes_list.html`, `notes_detail.html`, and `notes_popular.html`, I used Bootstrap classes such as:
	- `container`
	- `row`
	- `col`
	- `border`
	- `rounded`
	- `bg-primary`
	- `text-white`
	- `my-5`

### Why this matters

Bootstrap gives fast, ready-made styling patterns, while custom CSS lets you fine-tune the app with your own visual choices. Together, they give you speed plus flexibility.

### What I can already see in the project

- `notes_list.html` now displays notes in a grid layout instead of a plain list.
- `notes_detail.html` shows the note content inside a bordered area.
- `notes_popular.html` uses stronger visual emphasis with a colored card-like block and likes count.

---

## Code changes log (branch 05)

| Step | File | Change summary | Reason |
|---|---|---|---|
| 1 | `smartnotes/settings.py` | Added `STATICFILES_DIRS` and template directory entry | So Django can find shared static assets and `base.html` |
| 2 | `static/templates/base.html` | Created a reusable base template with Bootstrap | So all pages can share one layout |
| 3 | `static/css/style.css` | Added custom CSS classes | So the project can have custom styling beyond Bootstrap |
| 4 | `notes/templates/notes/notes_list.html` | Extended `base.html` and used Bootstrap grid classes | So notes render in a cleaner responsive layout |
| 5 | `notes/templates/notes/notes_detail.html` | Extended `base.html` and styled note detail content | So a single note page has structure and spacing |
| 6 | `notes/templates/notes/notes_popular.html` | Extended `base.html` and added visual emphasis | So popular notes stand out more clearly |

---

## Quick checks I can run mentally or in the browser

1. Visit the notes pages in the browser.
Expected result: they should share the same base structure and spacing.

2. Confirm templates extend the base template.
Expected result: `notes_list.html`, `notes_detail.html`, and `notes_popular.html` should all use `{% extends "base.html" %}`.

3. Confirm Bootstrap classes affect layout.
Expected result: notes should appear with spacing, borders, and grid alignment instead of unstyled plain text.

---

## New Django concepts learned in this module

| Concept | What it means | Example from my code |
|---|---|---|
| Static files | Non-Python assets like CSS, JS, and images | `static/css/style.css` |
| `STATICFILES_DIRS` | List of local folders Django searches for static assets | `BASE_DIR / 'static/'` in `smartnotes/settings.py` |
| Template inheritance | One template extends another shared layout | `{% extends "base.html" %}` |
| Template blocks | Named sections child templates can replace | `{% block content %}` in `base.html` |
| Bootstrap CDN | External stylesheet link for quick UI styling | Bootstrap link in `base.html` |

---

## Beginner summary

This stage was about making the Django app look more like a real website instead of a collection of plain HTML pages.

The main progression was:

1. Tell Django where static files live
2. Create one shared base template for all pages
3. Reuse that base template in page-specific templates
4. Add style with Bootstrap and custom CSS

That combination makes future front-end work faster, cleaner, and easier to maintain.