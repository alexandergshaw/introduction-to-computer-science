# Assignment 12 — Advanced Unit Testing

Week 12: functions worth testing across many inputs (think parametrized tests). Pay attention to the edge cases described below.

## What to build

1. `clamp(n, low, high)` — return `n` limited to the inclusive range `[low, high]`: `n` itself if it's already inside the range, otherwise the nearest boundary (`low` if too small, `high` if too big).
   - Helpful example: `clamp(5, 0, 10)` → `5`; `clamp(15, 0, 10)` → `10`; `clamp(-4, 0, 10)` → `0`
2. `in_range(n, low, high)` — return `True` if `n` is between `low` and `high` (inclusive), otherwise `False`.
   - Helpful example: `in_range(5, 0, 10)` → `True`; `in_range(15, 0, 10)` → `False`
3. `sign(n)` — return `1` if `n` is positive, `-1` if `n` is negative, and `0` if `n` is zero.
   - Helpful example: `sign(-3)` → `-1`; `sign(0)` → `0`; `sign(8)` → `1`

## Helpful examples & notes

- `min(x, y)` returns the smaller of two values; `max(x, y)` returns the larger.
- Python allows chained comparisons, e.g. `low <= n <= high`.

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
