# Django Challenge — class_05: Dividing a Template into Smaller Parts

![example 1: "welcome.html" from the video](./screenshots/Screenshot%20from%202026-05-11%2021-01-32.png)

The main goal of this challenge is to break down your HTML templates into modular, reusable pieces. While template inheritance (using `{% extends %}`) helps you avoid repeating your page structure, sometimes you want to include snippets of content from one template into another.

![example 2: "welcome.html" and "advantages.html" from the video](./screenshots/Screenshot%20from%202026-05-11%2021-01-48.png)

![example 3: "advantages.html" injected into "welcome.html" from the video](./screenshots/Screenshot%20from%202026-05-11%2021-02-06.png)

Think of it like modularizing code: just as you break a large function into smaller helper functions, you can break a large template into smaller template files and include them where needed.

---

## Steps

**Step 1: Understand the difference between template inheritance and inclusion**

Before you write any code, clarify the distinction:

- **Template inheritance** (`{% extends %}`): Used when a child template wants to override blocks defined in a parent template. One template "extends" another.
- **Template inclusion** (`{% include %}`): Used when you want to insert the entire content of one template into another at a specific location. The included template is treated like a snippet.

Think about the use case: if you want to add a separate "benefits" or "advantages" section to your welcome page *without* making it a child template, which approach should you use?

**Step 2: Create a new template file for advantages**

In your `templates/` directory (or appropriate template folder), create a new file called `advantages.html`.

This file should:
- Contain a list of benefits or advantages of your app
- Be a standalone HTML snippet (it does *not* need to be a complete HTML document with `<html>`, `<head>`, etc.)
- Include meaningful content that would be useful to display on the welcome page

For example, it could list features like "Easy to use", "Fast", "Organized", etc.

**Step 3: Understand template inclusion syntax**

Look up the Django template tag used to include one template inside another. It's a simple one-line syntax: `{% include "template_name.html" %}`.

You'll need to:
- Know the correct syntax
- Understand that the path is relative to your templates directory
- Recognize that the included template has access to the same context variables as the parent template

**Step 4: Modify the welcome template**

In your `welcome.html` template, add the `{% include %}` tag to insert the advantages section.

Decide where it makes sense to place it — perhaps after the main welcome message, or in a dedicated section of the page.

**Step 5: Test the result**

Visit your welcome page in the browser (or run the development server if it's not already running) and verify that:
- The advantages section appears where you included it
- The content is formatted and displayed correctly
- The page still functions as expected

---

## Additional quiz (created by the model, not by the LinkedIn Learning instructor)

This mini-quiz was added by me (the model) as extra practice. It is not part of the official course instructor content.

1. What is the difference between `{% extends %}` and `{% include %}`? When would you use each one?
2. When you `{% include %}` a template, does it have access to the parent template's context variables? Why or why not?
3. What would happen if you put a complete HTML document (with `<html>`, `<head>`, `<body>` tags) inside an included template?
4. Can you use template variables and conditionals inside an included template?
5. What is the file path syntax when including a template nested in a subdirectory? For example, if you have `templates/partials/header.html`, how would you include it?

Quick self-check answers (no peeking until you've tried!):
1. `{% extends %}` establishes an inheritance relationship where the child template fills in blocks defined by the parent (one parent, one child at a time). `{% include %}` inserts the content of one template as a snippet into another at a specific location (a template can include many others). Use `extends` for page layouts, use `include` for reusable content snippets.
2. Yes, it has access to the parent template's context because it's rendered in the same context. The included template is part of the same rendering pipeline and receives all the context variables the parent received.
3. You'd end up with nested HTML tags (multiple `<html>`, `<head>`, `<body>` tags inside the body of the parent), which would break the HTML structure and likely cause rendering issues. Included templates should be snippets, not complete documents.
4. Yes, absolutely. Included templates are still Django templates, so they support template variables (`{{ variable }}`), conditionals (`{% if %}`), loops (`{% for %}`), and all other template tags.
5. Use the path relative to the templates directory: `{% include "partials/header.html" %}`.

---

## What we actually did in this class

### Your solution

You implemented the challenge exactly with template inclusion and kept the page modular.

**Welcome template (`home/templates/home/welcome.html`)**

You placed the include inside a styled container under the main welcome content:

```html
{% extends "base.html" %}

{% block content %}
<div class="p-3 border rounded">
	<h1>Welcome to SmartNotes</h1>
	<p>This is the home page.</p>
	<p>Today is {{ today }}</p>
	<a href="{% url 'notes.list' %}" class="btn btn-primary">Check out these smartnotes!</a>

	<div class="p-3 border rounded mt-3">
		{% include "advantages.html" %}
	</div>
</div>
{% endblock %}
```

**Advantages snippet (`home/templates/home/advantages.html`)**

You created a reusable snippet with Bootstrap list styling:

```html
<h4>Advantages of Our App</h4>
<ul class="list-group">
	<li class="list-group-item list-group-item-success">Easy to use</li>
	<li class="list-group-item list-group-item-secondary">Fast</li>
	<li class="list-group-item list-group-item-warning">Organized</li>
</ul>
```

**Template discovery adjustment**

You also updated the Django template settings so this include path resolves correctly in your setup by adding `home/templates/home` to `DIRS`.

---

### Instructor's solution

The instructor also used inclusion, but referenced the template with a namespaced path:

```html
{% extends "base.html" %}

{% block content %}
	<h1>Welcome to SmartNotes!</h1>
	<p>Today is {{ today }}</p>
	<a href="{% url 'notes.list' %}" class="btn btn-primary">Check out these smartnotes!</a>

	<h2 class="my-5">Some advantages of our app:</h2>
	{% include "home/advantages.html" %}
{% endblock %}
```

The key difference in pathing is:
- Your include: `{% include "advantages.html" %}`
- Instructor include: `{% include "home/advantages.html" %}`

---

### Comparison

| Aspect | Your solution | Instructor's solution |
|---|---|---|
| Inclusion concept | Uses `{% include %}` correctly | Uses `{% include %}` correctly |
| Include path | `advantages.html` | `home/advantages.html` |
| Template config dependency | Relies on `DIRS` including `home/templates/home` | Works naturally with app-template namespacing |
| Welcome page structure | Wrapped in bordered Bootstrap containers | Simpler page flow with heading before include |
| Advantages content | In snippet with styled list-group items | Included as separate snippet path under `home/` |

Both approaches are valid and accomplish the challenge goal.

---

### Summary

You solved the challenge correctly and demonstrated the intended skill: dividing a larger template into smaller reusable parts with `{% include %}`.

Big takeaway from your implementation vs the instructor's:
- You proved that a short include path can work when template settings are configured to match it.
- The instructor showed a more explicit namespaced path (`home/advantages.html`), which is often clearer and scales well in multi-app projects.

In practice, both are acceptable, but explicit app-prefixed template paths are usually easier to reason about as a Django project grows.
