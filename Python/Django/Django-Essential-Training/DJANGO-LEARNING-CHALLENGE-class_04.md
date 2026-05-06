# Django Challenge — class_04: Showing Just Popular Notes

The main goal of this challenge is to create a second list view that displays only the notes considered "popular" — that is, notes that have more than one like.

Think of it like adding a filtered window into your data: instead of showing everything in the table, you want to show only the rows that meet a specific condition.

---

## Steps

**Step 1: Understand how `ListView` retrieves data**

Before you can filter the data, you need to understand how Django's `ListView` works under the hood.

By default, `ListView` retrieves all objects from the model you assign to it. Look at the existing `NotesListView` in `notes/views.py` and trace how it decides what to display. Which attribute tells it what model to use? How does it know what queryset to return?

Hint: look into `model` and `queryset` attributes on the class, and the `get_queryset()` method.

**Step 2: Create a new view for popular notes**

In `notes/views.py`, create a new class-based view called `NotesPopularListView`.

It should:
- Inherit from `ListView` (same as the existing notes list view)
- Use the same model and template logic as `NotesListView`

At this stage, don't worry about the filter yet — just get the new view wired up and returning something.

**Step 3: Override `get_queryset()` to apply a filter**

Override the `get_queryset()` method on your new view to return only notes with more than one like.

Django querysets support field lookups for comparisons like "greater than". You'll need to use the right lookup to filter by the `likes` field.

Think about:
- Which method on a queryset filters by a condition?
- What is the Django field lookup for "greater than"?

**Step 4: Register the new URL**

In `notes/urls.py`, add a new URL pattern that maps a path to your new `NotesPopularListView`.

Choose a path that clearly reflects what the view shows — for example, something under the existing notes URLs.

**Step 5: Create or reuse a template**

Decide whether your popular notes view needs its own template, or whether it can reuse the existing `notes_list.html`.

If you reuse the existing template, make sure the `template_name` attribute on your new view points to it.

---

## Additional quiz (created by the model, not by the LinkedIn Learning instructor)

This mini-quiz was added by me (the model) as extra practice. It is not part of the official course instructor content.

1. What is the difference between filtering at the view level with `get_queryset()` vs filtering in a template with `{% if %}`?
2. Why is it better to override `get_queryset()` than to set a static `queryset` class attribute when the filter depends on runtime data?
3. What Django queryset method and field lookup would you use to filter notes where `likes` is greater than 1?
4. What would happen if you did not override `get_queryset()` — what would the view display by default?

Quick self-check answers (no peeking until you've tried!):
1. Filtering at the view level hits the database only for the rows you need; filtering in the template loads all rows and discards them in Python, wasting memory and database work.
2. A static `queryset` attribute is evaluated once at class definition time; `get_queryset()` runs on every request, allowing dynamic filters (e.g., based on the current user or query parameters).
3. `Notes.objects.filter(likes__gt=1)` — `.filter()` is the method, `__gt` is the "greater than" lookup.
4. It would return all notes, because the default `get_queryset()` in `ListView` returns `model.objects.all()`.

---

## What we actually did in this class

### Your solution

**View (`notes/views.py`)**

You explored both approaches, first trying the `queryset` class attribute (commented out), then settling on `get_queryset()`:

```python
class NotesPopularListView(ListView):
    model = Notes
    # queryset = Notes.objects.filter(likes__gt=0)  # 1st approach
    context_object_name = "notes"
    template_name = "notes/notes_popular.html"

    def get_queryset(self):  # 2nd approach
        return Notes.objects.filter(likes__gt=0)
```

**Template (`notes/templates/notes/notes_popular.html`)**

You created a dedicated template and added the like count to each row:

```html
<html>
    <h1>Popular Notes</h1>
    {% for note in notes %}
        <h3>{{note.title}} - # of Likes: {{note.likes}}</h3>
    {% endfor %}
</html>
```

**URL (`notes/urls.py`)**

```python
path('notes/popular', views.NotesPopularListView.as_view()),
```

---

### Instructor's solution

```python
class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(likes__gte=1)
```

The instructor reused the existing `notes_list.html` template and used the `queryset` class attribute instead of `get_queryset()`.

---

### Comparison

**Filter condition: `likes__gt=0` vs `likes__gte=1`**

These are logically equivalent for whole numbers — "greater than 0" and "greater than or equal to 1" return the same rows when `likes` is an integer. Your choice is fine; the instructor's `gte=1` reads slightly more like natural English ("at least 1 like"), but it makes no practical difference here.

**`get_queryset()` method vs `queryset` class attribute**

This is the most interesting difference. You went further than the instructor by using `get_queryset()`.

- The `queryset` class attribute is evaluated **once** when the class is defined (at server startup). It works fine for static filters like this one, but it cannot react to runtime data (the current user, query parameters, URL kwargs, etc.).
- `get_queryset()` runs **on every request**, making it the correct pattern whenever the filter might need to change based on context.

For this specific challenge, both work identically. But your instinct to explore `get_queryset()` was the right move — it's the more powerful and more common real-world pattern.

**Template: new `notes_popular.html` vs reusing `notes_list.html`**

The instructor reused the existing template for simplicity. You created a dedicated one and added the like count to the display, which is actually more useful for a "popular notes" view. Neither is wrong; it depends on the product requirement.

---

### Summary

| Aspect | Your solution | Instructor's solution |
|---|---|---|
| Filter logic | `likes__gt=0` | `likes__gte=1` |
| Practical result | Identical | Identical |
| Implementation pattern | `get_queryset()` | `queryset` attribute |
| Flexibility | Higher (runtime-aware) | Lower (static) |
| Template | New, shows like count | Reuses existing |

You went one level deeper than required, which is a good habit. The only thing to keep in mind is that when a static attribute is enough (no runtime data needed), the `queryset` attribute is simpler and more readable — but knowing `get_queryset()` and when to reach for it is the more important skill.
