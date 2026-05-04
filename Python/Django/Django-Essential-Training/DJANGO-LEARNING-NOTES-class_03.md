# Django Learning Notes — class_03
## How Django Interacts with Databases

---

## 1. Introduction to ORMs

An ORM (Object-Relational Mapper) lets you interact with a database using Python objects instead of writing raw SQL.

Django's built-in ORM translates Python class definitions into database tables, and Python method calls into SQL queries — so you never have to write SQL manually for common operations.

Example mental model:

| Python | Database |
|---|---|
| A model class (e.g. `Notes`) | A table |
| A class attribute (e.g. `title`) | A column |
| An instance of the class | A row |

---

## 2. Creating your first model

A model is a Python class that inherits from `django.db.models.Model`.
Each attribute on the class becomes a column in the database table.

Created the `notes` app and defined the `Notes` model in `notes/models.py`:

```python
from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
```

Field types used:

| Field | Purpose |
|---|---|
| `CharField(max_length=200)` | Short text with a character limit (e.g. a title) |
| `TextField()` | Long-form text with no length limit (e.g. a note body) |
| `DateTimeField(auto_now_add=True)` | Stores the date and time automatically when the record is first created |

> Django automatically adds an `id` primary key field to every model.

### Steps to activate a new model

1. Register the app in `smartnotes/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'notes',
]
```

2. Generate the migration file:

```bash
python manage.py makemigrations
```

3. Apply the migration to the database:

```bash
python manage.py migrate
```

---

## 3. Using admin for data creation and manipulation

Django ships with a built-in admin panel at `/admin/` where you can create, read, update and delete records visually without writing any views or templates.

To expose a model in the admin, register it in `notes/admin.py`:

```python
from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)
```

What each part does:
- `NotesAdmin` customises how the model appears in the admin interface.
- `list_display` defines which fields are shown as columns in the list view.
- `admin.site.register(...)` connects the model and its admin config to the admin panel.

---

## 4. Using Django shell for creating and querying data

The Django shell is an interactive Python prompt with your full project loaded.
It lets you run ORM queries directly to test or inspect data.

```bash
python manage.py shell
```

### Importing your model

```python
from notes.models import Notes
```

### Creating records

```python
# Create and save a record in one step
Notes.objects.create(title="My first note", text="This is the note body.")
```

### Retrieving records

```python
# Get all records
Notes.objects.all()

# Get a single record by primary key
Notes.objects.get(pk=1)

# Filter records — returns a QuerySet (like a list)
Notes.objects.filter(title="My first note")
```

### Querying with field lookups

Django's ORM supports field lookups to perform flexible searches.
They are written as `fieldname__lookuptype="value"`.

| Lookup | Meaning | Example |
|---|---|---|
| `icontains` | Case-insensitive substring match | `title__icontains="django"` matches "Django", "DJANGO", "my django note" |
| `contains` | Case-sensitive substring match | `title__contains="Django"` |
| `exact` | Exact value match (default) | `title__exact="Django"` |
| `startswith` | Value starts with string | `title__startswith="My"` |

### Chaining filter and exclude

```python
Notes.objects.filter(text__icontains="Django").exclude(title__icontains="Django")
```

Breaking this down step by step:

1. `Notes.objects` — the query manager, the entry point to all database queries for the Notes model.
2. `.filter(text__icontains="Django")` — keep only records whose `text` field contains the word "Django" (case-insensitive).
3. `.exclude(title__icontains="Django")` — from those results, remove any record whose `title` also contains "Django".

Result: notes that mention Django in the body but whose title does not mention Django.

> Chaining `.filter()` and `.exclude()` returns a QuerySet — a lazy list of matching records.
> The actual database query only runs when you access or print the results.
