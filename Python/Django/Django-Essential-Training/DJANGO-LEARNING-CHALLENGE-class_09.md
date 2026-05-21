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

## Compare Later Section (leave blank for now)

When you finish your implementation and watch the instructor solution, we can complete:
- Your approach
- Instructor's approach
- Side-by-side comparison
- Final takeaways
