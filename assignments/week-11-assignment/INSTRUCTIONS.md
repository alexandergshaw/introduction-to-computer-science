# Assignment 11 — Unit Testing

Week 11: small, predictable functions that are easy to test, including their edge cases. Build the three functions described below.

## What to build

1. `is_palindrome(s)` — return `True` if `s` reads the same forwards and backwards, ignoring capitalisation; otherwise `False`.
   - Helpful example: `is_palindrome("racecar")` → `True`; `is_palindrome("hello")` → `False`
2. `is_even(n)` — return `True` if the whole number `n` is even; otherwise `False`.
   - Helpful example: `is_even(4)` → `True`; `is_even(7)` → `False`
3. `absolute(n)` — return the absolute value of `n` — its distance from 0, which is never negative.
   - Helpful example: `absolute(-3)` → `3`; `absolute(5)` → `5`

## Helpful examples & notes

- A string has a `.lower()` method (a lowercase copy), useful for ignoring capitalisation.
- Slice notation can reverse a sequence — look up the `[::-1]` slice.
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
