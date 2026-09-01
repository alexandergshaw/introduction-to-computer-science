# Assignment 10 — Error Handling and File I/O

Week 10: using try / except so your code reacts to errors instead of crashing. Each function attempts a normal action and returns a safe fallback if it fails.

## What to build

1. `safe_divide(a, b)` — return `a` divided by `b`. If `b` is 0, return `None` instead of crashing.
   - Helpful example: `safe_divide(6, 2)` → `3`; `safe_divide(1, 0)` → `None`
2. `to_int(text, default=0)` — return `text` converted to an integer. If `text` isn't a valid whole number, return `default` instead.
   - Helpful example: `to_int("42")` → `42`; `to_int("abc")` → `0`; `to_int("abc", -1)` → `-1`
3. `safe_get(items, index)` — return the item at position `index` in `items`. If `index` is out of range, return `None`.
   - Helpful example: `safe_get([10, 20, 30], 1)` → `20`; `safe_get([10, 20, 30], 9)` → `None`

## Helpful examples & notes

- Code that might fail goes in a `try:` block; an `except SomeError:` block runs only when that specific error happens.
- Dividing by 0 raises `ZeroDivisionError`, `int("abc")` raises `ValueError`, and an out-of-range list index raises `IndexError`.

> Tip: open `test_assignment.py` to see the exact inputs and expected outputs.

## How to complete this module (no terminal)

1. Open this repository in **Codespaces** from the GitHub **Code** button.
2. **Create a branch off `main`** before you change anything:
   - Open the branch selector at the top-left of the file list and make sure **`main`** is selected.
   - Type a new branch name (for example, `your-name-this-module`).
   - Click **Create branch** — it will branch from `main`.
   - Confirm your Codespace / editor is now on your new branch, not `main`.
3. In the file explorer, open `student_work.py` in this folder.
4. Complete the TODOs in `student_work.py`.
5. Click the **Testing** beaker icon and run `test_assignment.py`.
6. Keep editing until all tests pass.
7. Use the **Source Control** icon to review your changes.
8. Enter a commit message and click **Commit**.
9. Click **Sync Changes** to push your branch to GitHub.
10. **Open a Pull Request back into `main`:**
    - In GitHub, click **Compare & pull request** for your branch.
    - Set the **base** branch to **`main`** and the **compare** branch to your branch.
    - Add a title and short description, then click **Create pull request**.
11. After the checks pass, **Merge the Pull Request into `main`**, then delete your branch.
