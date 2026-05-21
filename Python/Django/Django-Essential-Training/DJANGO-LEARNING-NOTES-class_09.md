# Django Learning Notes — class_09: Authentication Flows and Public Sharing

## Module Overview

This module continues the user-specific workflow and introduces authentication UX and public-sharing features. These notes are started with chapter 1 and prepared for incremental updates as the module progresses.

---

## Chapters and Key Learnings

### 1. Adding login and logout pages

#### What the transcript covers
- Create a login page using Django auth class-based views (`LoginView`).
- Set `template_name` to render the custom login template.
- Configure login route and login form using POST with CSRF.
- Fix redirect after login by setting `LOGIN_REDIRECT_URL` in project settings.
- Add logout route and logout template with `LogoutView`.

#### What was implemented in this project
- `LoginInterfaceView` and `LogoutInterfaceView` were implemented in the home app.
- URLs for login/logout were configured in `home/urls.py`.
- Login template posts correctly using CSRF and works with `LOGIN_REDIRECT_URL`.
- Logout action was moved to a POST form in base layout so authenticated users can log out from anywhere.
- A dedicated farewell route (`/farewell/`) was added and used as logout redirect target.
- Farewell page now auto-redirects to the welcome page (`/`) after a short delay.

#### Troubleshooting and differences from the transcript
- In current Django (your project uses Django 6.0.4), `LogoutView` rejects GET requests.
- This causes `Method Not Allowed (GET): /logout/` when visiting `/logout/` directly in the browser.
- This is expected behavior in newer versions and not a bug in your app.
- Practical fix used: send logout through a POST form with `{% csrf_token %}`.
- Important consequence: a `logout.html` page is not part of the main logout flow when logout happens via POST + redirect.

#### Extra notes to keep
- Keep logout as POST-only for security and framework compatibility.
- Keep `LOGOUT_REDIRECT_URL` pointing to a non-logout page (currently `/farewell/`), so post-logout navigation is clear.
- If you want a farewell page, use a separate route/template instead of relying on GET `/logout/`.

### 2. Adding a signup page

#### What the transcript covers
- Add a dark navbar in the shared base template.
- Show Login when user is anonymous, and Home + Logout when user is authenticated.
- Clarify version-specific logout behavior:
	- Django 4.x and below: logout can be link-based (GET).
	- Django 5.0+: logout must be POST.
- For Django 5.0+, wrap logout in a POST form with CSRF token.

#### Instructor gap noted
- In the chapter titled "Adding a signup page", the transcript content does not actually show signup page creation.
- The real signup behavior appears only later (in finishing touches), where the flow assumes signup already exists.
- This can confuse students because the title and the demonstrated steps do not match.

#### What was implemented in this project
- A navbar was added in the active base template with conditional rendering based on `user.is_authenticated`.
- Anonymous users see a Login button.
- Anonymous users also see a Sign Up button.
- Authenticated users see Home and Logout controls.
- Logout is implemented as POST form + CSRF (compatible with Django 5+/6.x).
- The project keeps a reference template (`base_template_rf.html`) and an active template (`base.html`) to preserve learning history while using the secure workflow.
- Signup flow was completed manually in the app:
	- Added `SignupView` using `UserCreationForm`.
	- Added URL route `signup/` named `signup`.
	- Added `home/signup.html` template with POST + CSRF + form rendering.
	- On successful signup, redirect goes to login so the new user can authenticate.

#### Before and after (signup gap fix)

Before (placeholder, no real signup logic):

```python
class SignupView(TemplateView):
	template_name = 'home/signup.html'
```

After (functional signup):

```python
class SignupView(FormView):
	template_name = 'home/signup.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)
```

Route added:

```python
path('signup/', views.SignupView.as_view(), name='signup')
```

#### Troubleshooting and differences from the transcript
- Your comments in both base templates correctly capture the core issue: GET logout from older examples fails on newer Django with 405.
- The practical fix is exactly what you implemented: use a form that POSTs to `/logout/` with CSRF.
- In your current workflow, logout then redirects to `/farewell/` (`LOGOUT_REDIRECT_URL`), not directly to login.
- This means the old expectation of visiting `/logout/` as a page is no longer valid in the main flow.

#### Extra notes to keep
- Keep `base.html` as the active template for production flow and `base_template_rf.html` as historical/reference material.
- Keep logout as POST-only in navbar controls.
- Keep Home/Login/Logout visibility tied to authentication state for cleaner UX.

### 3. Finishing touches

#### What the transcript covers
- Consolidates navbar behavior with conditional controls.
- For authenticated users: show Home, Create, and Logout controls.
- For anonymous users: show Login and Signup.
- Demonstrates full cycle: signup -> redirect to login -> login -> create note as new user.

#### What was implemented in this project
- Navbar now supports auth-aware controls in the active base template.
- Signup route is functional and linked from navbar.
- New users can register outside Django admin and then create their own notes after login.
- Logout remains POST-only for Django 5.0+ compatibility.

#### Troubleshooting and differences from the transcript
- Transcript uses mixed logic across chapters; actual signup implementation steps were missing earlier and had to be completed in this project.
- Current implementation explicitly fills that gap with a working form/view/URL/template flow.

#### Before and after (logout for Django 5+)

Before (works on older versions, fails on Django 5+):

```html
<a href="{% url 'logout' %}" class="btn btn-outline-light me-1">Logout</a>
```

After (compatible with Django 5+/6.x):

```html
<form action="{% url 'logout' %}" method="post" class="d-inline">
	{% csrf_token %}
	<button type="submit" class="btn btn-outline-light me-1">Logout</button>
</form>
```

### Extra Refactor (Not in the Course): Popular Notes Privacy

#### Problem observed
- Popular notes page was listing notes across all users, including private notes from other users.

#### Goal
- Keep popular ranking, but respect visibility boundaries.

#### Step-by-step refactor
1. Import `Q` from Django ORM in `notes/views.py`.
2. Update `NotesPopularListView.get_queryset()` to filter by likes and visibility rules.
3. Keep ordering by `-likes`.

Before:

```python
return Notes.objects.filter(likes__gt=0).order_by('-likes')
```

After:

```python
return Notes.objects.filter(
	Q(likes__gt=0) & (Q(user=self.request.user) | Q(is_public=True))
).order_by('-likes')
```

#### Result
- Users still see popular notes.
- Private notes are only visible to their owner.
- Public notes from other users can appear safely.

### 4. Code challenge: Create a share link for a public note

Pending notes.

### 5. Solution: Create a share link for a public note

Pending notes.

---

## Current Validation Status

- Django project check runs successfully (`python manage.py check`).
- Auth flow is consistent with current Django behavior when logout is sent by POST.

---

## Suggested Improvements (current chapter)

- Keep `LOGOUT_REDIRECT_URL` on a non-logout page (current setup `/farewell/` is correct).
- Keep the logout button only as a POST form in shared layout.
- Remove `{{ form.as_p }}` from `logout.html` if that template is kept for reference, since `LogoutView` does not need a user form in this POST-only pattern.

---

## References

- `home/views.py`
- `home/urls.py`
- `home/templates/home/login.html`
- `home/templates/home/logout.html`
- `static/templates/base.html`
- `static/templates/base_template_rf.html`
- `smartnotes/settings.py`
- `transcript.txt`
