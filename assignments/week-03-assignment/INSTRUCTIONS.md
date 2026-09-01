# Assignment 03 — Logic and Control Flow

Week 3: comparisons and if / elif / else. Three short decisions.

## What to build

1. `classify(n)` — return `"positive"` if `n` is greater than 0, `"negative"` if it is less than 0, and `"zero"` if it is exactly 0.
   - Helpful example: `classify(5)` → `"positive"`; `classify(0)` → `"zero"`
2. `is_even(n)` — return `True` if the whole number `n` is even, otherwise `False`.
   - Helpful example: `is_even(4)` → `True`; `is_even(7)` → `False`
3. `larger(a, b)` — return whichever of `a` and `b` is larger.
   - Helpful example: `larger(3, 9)` → `9`

## Helpful examples & notes

- A comparison such as `n > 0` evaluates to `True` or `False`.
- if / elif / else lets your code choose between different branches.
- The `%` (modulo) operator gives the remainder left after a division.

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
