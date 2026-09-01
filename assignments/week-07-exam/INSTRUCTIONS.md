# Exam 07 — Exam 1

Practice exam covering Weeks 0–6 (data types, control flow, functions, and data structures). Three short problems at the same level as the weekly work.

## What to build

1. `letter_grade(score)` — return the letter grade for a numeric score (0–100) using the standard cutoffs: 90+ = A, 80+ = B, 70+ = C, 60+ = D, anything below 60 = F.
   - Helpful example: `letter_grade(95)` → `"A"`; `letter_grade(72)` → `"C"`; `letter_grade(40)` → `"F"`
2. `average(nums)` — return the average (mean) of the numbers in `nums`.
   - Helpful example: `average([2, 4, 6])` → `4`
3. `count_positives(nums)` — return how many numbers in `nums` are greater than 0.
   - Helpful example: `count_positives([-1, 2, 0, 5])` → `2`; `count_positives([-3, -2])` → `0`

## Helpful examples & notes

- if / elif checks run top to bottom and the first true one wins, so the order of your cutoffs matters.
- `len(list)` is how many items a list holds; `sum(list)` adds up its numbers.

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
