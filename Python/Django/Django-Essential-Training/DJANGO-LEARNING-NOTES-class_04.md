# Django Learning Notes - class_04
## Building Dynamic Webpages

---

## Module 04 chapters covered

1. Creating a dynamic template
2. Creating your first Django dynamic webpage
3. How Django can list data with just some small changes
4. Introduction to Django class-based views
5. Code challenge: showing just popular notes
6. Solution: showing just popular notes

---

## 1. Creating a dynamic template

In this module, the page moved from static output to template-driven rendering.
The key idea is to let views pass context data to templates and have Django render the final HTML.

In practice, this means:
- View logic decides what data is needed.
- Template logic decides how to present that data.
- Django combines both into the response.

---

## 2. Creating your first dynamic webpage

You updated the home flow from function-based views toward class-based views using `TemplateView`.

### What changed

In `home/views.py`:
- Added `HomeView(TemplateView)` with `template_name = 'home/welcome.html'`.
- Passed `today` through `extra_context`.
- Added `AuthorizedView(LoginRequiredMixin, TemplateView)` with `template_name = 'home/authorized.html'` and `login_url = '/admin'`.

In `home/urls.py`:
- Switched to class-based routing with `.as_view()`.

```python
urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
]
```

### Why `.as_view()` is required

Class-based views are classes, not callable functions.
`.as_view()` returns a callable view function that Django can attach to a URL pattern.

---

## 3. Important routing lesson: trailing slash and 404 behavior

You observed that after converting to class-based views, `home` and `authorized` without trailing slash produced 404, while adding `/` fixed it.

### Why this happens

Django URL matching is exact against the declared route pattern.
If your route is declared as `path('home/', ...)`, then:
- `/home/` matches directly.
- `/home` does not directly match.

If `APPEND_SLASH=True` (default) and `CommonMiddleware` is active, Django may redirect `/home` to `/home/` for safe methods (like GET). If that middleware behavior is not applied in a specific flow, you can still see a 404.

### Best practice to avoid this issue

- Define URL patterns consistently with trailing slashes for page endpoints.
- Access those endpoints with trailing slashes.
- Keep `APPEND_SLASH=True` and `CommonMiddleware` enabled in normal project settings.

This avoids ambiguity and keeps route behavior predictable.

---

## 4. Listing and detail pages with class-based views

In `notes/views.py`, you implemented generic CBVs:

```python
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
```

In `notes/urls.py`, routes were added for list, detail, and popular views:

```python
urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    path('notes/popular', views.NotesPopularListView.as_view()),
]
```

And in `smartnotes/urls.py`, the notes app routing was included under:

```python
path('smart/', include('notes.urls'))
```

So the notes URLs are now nested under `/smart/`.

---

## 5. Template naming convention with generic CBVs

Django generic views can infer template names automatically.

For model `Notes`:
- `ListView` defaults to `notes/notes_list.html`
- `DetailView` defaults to `notes/notes_detail.html`

That means explicitly setting `template_name` for `NotesListView` is optional if you follow naming conventions.

However, for the custom popular list page, setting a custom template path is necessary when you want a separate template file:

```python
template_name = "notes/notes_popular.html"
```

---

## 6. Challenge: showing just popular notes

Goal: display only notes that are considered popular (notes with likes above a threshold).

### Your implemented approach

You created a dedicated view:

```python
class NotesPopularListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_popular.html"

    def get_queryset(self):
        return Notes.objects.filter(likes__gt=0)
```

You also created a dedicated template (`notes/templates/notes/notes_popular.html`) to show each note title plus its like count.

### Instructor approach (for comparison)

The instructor solution used:

```python
queryset = Notes.objects.filter(likes__gte=1)
template_name = "notes/notes_list.html"
```

### Comparison and learning point

- `likes__gt=0` and `likes__gte=1` are equivalent for integer likes.
- `queryset = ...` is static at class definition time.
- `get_queryset()` runs per request and is better for dynamic/runtime-dependent filtering.

For this challenge, both approaches work. Your `get_queryset()` choice is more extensible.

---

## 7. Extra references and artifacts used during learning

You referenced a Stack Overflow discussion about `queryset` vs `get_queryset()`:
- https://stackoverflow.com/questions/19707237/use-get-queryset-method-or-set-queryset-variable

Screenshot captured during the learning process:

![validation of `get_queryset()` approach](./screenshots/Screenshot%20from%202026-05-06%2017-14-29.png)
- `screenshots/Screenshot from 2026-05-06 17-14-29.png` (validation of `get_queryset()` approach)

---

## 8. Summary of what this branch demonstrates

- Migrating from function-based views to class-based views with `TemplateView` and `.as_view()`.
- Protecting class-based pages with `LoginRequiredMixin`.
- Understanding exact URL matching and trailing slash behavior.
- Using generic `ListView` and `DetailView` for low-boilerplate CRUD-style pages.
- Implementing filtered list pages via `get_queryset()`.
- Structuring project URLs with app-level routing via `include(...)`.

This module was a strong step from basic Django CRUD foundations into reusable, scalable view patterns.