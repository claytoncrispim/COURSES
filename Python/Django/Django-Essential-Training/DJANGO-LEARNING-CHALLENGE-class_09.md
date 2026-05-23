# Django Challenge — class_09: Create a Share Link for a Public Note

The main goal of this challenge is to add a shareable link for notes, while guaranteeing that only public notes are accessible through that link.

Challenge prompt (from the course transcript):
- Create a new view that does not require login.
- Expose notes through a share link.
- Ensure only public notes can be viewed from that link.
- Ensure private notes are never exposed to unauthorized users.

---

## Steps (Hints Only)

**Step 1: Define the sharing behavior clearly**

Before coding, decide exactly what the share link should do.

Hints:
- Shared page should be readable without authentication.
- Shared page should show a single note.
- Private notes must not be visible through this endpoint.

Think:
- What should happen if someone opens a share link to a private note?
- Should the response be "not found" or "forbidden"?

**Step 2: Create a dedicated public view**

Add a new endpoint view for shared notes, separate from authenticated detail pages.

Hints:
- Do not use `LoginRequiredMixin` for this one.
- Fetch the note by identifier and public visibility.
- Keep the lookup strict (identifier + `is_public=True`).

Think:
- Why is it safer to filter public status in the query itself?

**Step 3: Add URL route for share endpoint**

Create a route for the public share page.

Hints:
- Keep URL naming consistent with your project style.
- Include note identifier in the route.
- Use a clear route name for reversing from templates.

Think:
- Which route pattern will be easiest to use in templates and tests?

**Step 4: Add share action in authenticated note UI**

In note detail (or another authenticated page), add a way for owners to access/copy the share link.

Hints:
- Show share link controls only when `note.is_public` is true.
- If note is private, show a clear message guiding user to make it public first.
- Consider showing the full absolute URL for easy copy.

Think:
- What is the simplest user experience to avoid accidental sharing of private notes?

**Step 5: Create a template for public note view**

Build a template for the shared note page.

Hints:
- Keep it minimal and read-only.
- Show title/content and optional public badge.
- Avoid edit/delete/toggle controls in public view.

Think:
- Which actions should never appear on a public shared page?

**Step 6: Enforce privacy guarantees**

Double-check the view logic to prevent private-note leakage.

Hints:
- Never fetch by `pk` alone for public endpoint.
- Ensure private notes do not render through shared route.
- Re-test after refactors to avoid regressions.

Think:
- What happens if another user guesses a note ID?

**Step 7: Validate end-to-end behavior**

Test all key scenarios manually.

Checklist:
- Public note opens correctly via share link while logged out.
- Private note does not open via share link while logged out.
- Private note still opens for owner through authenticated detail page.
- Public/private toggle affects shared link availability as expected.
- Existing popular/list pages still respect visibility rules.

---

## Branch Context to Keep in Mind

Your branch has two important context factors that affect this challenge:

1. Signup was completed in-project (not fully explained in the course chapter)
- You now have full auth flow for non-admin users.
- Test shared-link behavior using a second normal user account created via signup.

2. Popular notes privacy refactor already exists
- Popular listing now respects visibility boundaries.
- Keep share endpoint aligned with the same privacy rule: only public notes are shareable.

---

## Pitfalls to Watch For

- Creating share endpoint with `LoginRequiredMixin` (breaks the challenge goal).
- Fetching by note ID only, without checking `is_public`.
- Showing share controls for private notes without guard rails.
- Reusing internal detail template and exposing edit/delete actions publicly.
- Returning detailed permission errors that reveal private note existence.
- Forgetting to test as logged-out user and as a second user.

---

## Additional Quiz (extra practice)

This mini-quiz is extra practice and not official instructor content.

1. Why should share endpoint be separate from authenticated detail endpoint?
2. Why is filtering by `is_public=True` in query safer than checking after fetch?
3. What public-view actions should be removed to keep it read-only?
4. How does signup support stronger testing for this challenge?
5. How is this challenge connected to your popular-notes privacy refactor?

---

## What this challenge evaluates

- Separation of authenticated vs public access paths.
- Privacy-aware querying and endpoint design.
- Safe template composition for public pages.
- Consistent visibility rules across app features.

---

## Solution Comparison (Completed)

The following section compares your final implementation with the instructor solution.

### Your Approach

- **View:**
	- Implemented a function-based `notes_share_view`.
	- Kept the endpoint public while enforcing note visibility checks before rendering.
	- Returned a share page that exposes a copyable absolute URL.

- **URL:**
	- Added `notes/<int:pk>/share` with the name `notes.share`.

- **Template:**
	- Built `notes_share.html` to show a public note, a shareable link, and a privacy warning for private notes.
	- Used the current request URL to help the owner copy the link.
	- Added a copy interaction for usability.

- **Privacy behavior:**
	- Public notes can be opened through the share link.
	- Private notes are blocked and shown with a protective fallback message.

### Instructor's Approach

- **View:**
	- Uses a class-based `NotesPublicDetailView`.
	- Removes `LoginRequiredMixin` so the page is public.
	- Filters the queryset so only `is_public=True` notes are eligible.

- **URL:**
	- Adds a share route that maps to the public detail view.

- **Template:**
	- Reuses the note detail template for the public share flow.
	- Keeps the implementation simpler and more direct.

### Side-by-Side Comparison

| Aspect | Your Approach | Instructor's Approach |
|---|---|---|
| View style | Function-based view | Class-based view |
| Permission handling | Custom logic in FBV | Queryset filtering in CBV |
| Share page | Dedicated share template | Reused detail template |
| Share link UX | Copyable absolute URL and explicit messaging | Simpler public detail rendering |
| Privacy | Explicit note-level checks and messages | Query-level restriction to public notes |

**Key Differences:**
- Your version is more explicit and user-guided, which is useful when you want to expose a copyable share URL and explain blocked private-note access.
- The instructor’s version is more compact and idiomatic for a pure public read-only page.

### Real-World Guidance

- Use a function-based view when the share flow needs custom branching, custom messages, or a very explicit permission rule.
- Use a class-based view when the page is structurally similar to an existing detail page and the main difference is queryset filtering.
- For production, the safest baseline rule is: only public notes can be queried in the public endpoint.

### Final Takeaways

- Never expose private notes through a public share link.
- Returning 404 for private notes is preferable to revealing that the note exists.
- Reusing a detail template can save time, but a dedicated share template gives you more control over UX.
- The safest design keeps sharing simple while making private content non-discoverable.
