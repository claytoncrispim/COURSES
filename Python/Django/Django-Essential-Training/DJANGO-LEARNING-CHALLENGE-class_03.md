# Django Challenge — class_03: Adding Likes to Notes

The main goal of this challenge is to enhance the `Notes` model by adding a new field to track how many likes each note has received.

Think of it like adding a new column to a spreadsheet that already has data in it — you need to decide what value the existing rows should get for that new column, and then tell the database about the change.

---

## Steps

**Step 1: Add a new field to the model**

Open `notes/models.py` and add a new attribute to the `Notes` class.
This attribute will represent the number of likes a note has received.

In Django, each attribute on a model class maps directly to a column in the database table — so adding an attribute here means adding a new column.

**Step 2: Choose the right field type**

Django provides many field types depending on the kind of data you want to store.
Since likes are a whole number (0, 1, 2, …), the right choice here is `IntegerField`.

```python
likes = models.IntegerField()
```

**Step 3: Handle existing records**

Your database already has notes in it. When you add a new column, the database needs to know what value to put in that column for all the rows that already exist.

You have two options:
- `default=0` — every existing note starts with 0 likes (most common for this case).
- `null=True` — the field is left empty (`NULL`) for existing records.

For a likes counter, a default of `0` makes the most sense:

```python
likes = models.IntegerField(default=0)
```

**Step 4: Apply database migrations**

After changing the model, you need to tell Django to update the database to match.
This is a two-step process:

```bash
# Step 4a — Generate the migration file (Django reads your model changes and writes the instructions)
python manage.py makemigrations

# Step 4b — Apply the migration (Django executes those instructions on the database)
python manage.py migrate
```

> Think of `makemigrations` as drafting the plan, and `migrate` as carrying it out.

---

## What we actually did in this class

Based on `notes/models.py`, this challenge was solved in two iterations.

### Your approach (first iteration)

```python
likes = models.IntegerField(null=True)
```

Why this works:
- It stores whole numbers.
- `null=True` allows existing rows to keep an empty value while you evolve the schema.

Trade-off:
- Likes should not be negative, but `IntegerField` allows negative values.
- `NULL` means "unknown" rather than "zero likes", which can make reporting and filtering less intuitive for this use case.

### Instructor approach (refined iteration)

```python
likes = models.PositiveSmallIntegerField(default=0)
```

Why this is better for likes:
- `PositiveSmallIntegerField` enforces non-negative numbers at the model level.
- `default=0` gives every existing and new note a clear starting value.
- The type communicates intent: likes are a small, non-negative counter.

### Range comparison (important)

Common Django integer field ranges:

| Field type | Typical signed range | Good for likes? |
|---|---|---|
| `IntegerField` | about `-2,147,483,648` to `2,147,483,647` | Works, but allows negatives and is broader than needed |
| `PositiveSmallIntegerField` | `0` to `32,767` | Better fit for most note-like apps |

Beginner rule of thumb:
- Use the narrowest field that correctly matches your business rule.
- Since likes cannot be negative, a positive field with `default=0` is usually the best choice.

### Migration history for this challenge

- `0002_notes_likes.py`: added `likes` as `IntegerField(null=True)` (your initial implementation)
- `0003_alter_notes_likes.py`: changed `likes` to `PositiveSmallIntegerField(default=0)` (instructor refinement)

---

> This challenge helps you practice one of the most common real-world tasks in Django development: evolving your data model as your application grows, without losing existing data.

---

## Additional quiz (created by the model, not by the LinkedIn Learning instructor)

This mini-quiz was added by me (the model) as extra practice. It is not part of the official course instructor content.

1. Why is `PositiveSmallIntegerField(default=0)` usually a better fit for likes than `IntegerField(null=True)`?
2. If your app could realistically exceed 32,767 likes on a note, what field type change might you consider and why?
3. What is the practical difference between `NULL` and `0` for a likes counter in queries and reports?
4. What does `makemigrations` do that `migrate` does not?

Quick self-check answers:
1. It prevents negative values and gives a clear default starting value.
2. A larger positive integer type (for example `PositiveIntegerField`) to support a wider range.
3. `NULL` means unknown/not set, while `0` means explicitly no likes.
4. `makemigrations` creates migration files; `migrate` applies them to the database.

