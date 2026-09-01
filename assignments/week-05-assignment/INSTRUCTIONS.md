# Assignment 05 — Data Structures

Week 5: lists and sets, plus some handy built-in helper functions.

## What to build

1. `unique_sorted(items)` — return a list of the unique values from `items`, sorted in ascending order.
   - Helpful example: `unique_sorted([3, 1, 2, 1])` → `[1, 2, 3]`
2. `total(nums)` — return the sum of all the numbers in `nums`.
   - Helpful example: `total([1, 2, 3])` → `6`
3. `largest(nums)` — return the largest number in `nums`.
   - Helpful example: `largest([4, 9, 2])` → `9`

## Helpful examples & notes

- A `set()` drops duplicate values; `sorted()` returns a new list in order.
- `sum()` adds up the numbers in a list; `max()` finds the largest item.

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
