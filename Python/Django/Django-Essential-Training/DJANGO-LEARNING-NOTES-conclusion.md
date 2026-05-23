# Django Learning Notes — Conclusion

## What This Course Built

This course finished with a Django application that supports:
- login and logout pages
- signup for new users
- user-specific notes
- public/private visibility control
- a public share link for notes

## Main Takeaways

- Django generic class-based views are a strong fit for standard CRUD pages.
- Function-based views are often better when the behavior is small, custom, or permission-sensitive.
- Public/private rules should be enforced in the queryset or endpoint, not only in the template.
- POST should be used for state-changing actions such as logout, liking, and visibility toggles.
- Private notes should never be exposed through public routes.

## What to Do Next

- Practice unit testing in Django.
- Explore Django REST framework if you want API endpoints.
- Keep building small features on top of the current app.
- Review the official Django documentation as a reference while coding.

## Personal Note

The biggest lesson from this course is that small design choices matter: the right mix of CBVs, FBVs, queryset filters, and template guards makes the application both safer and easier to maintain.
