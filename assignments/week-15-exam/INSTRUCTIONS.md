# Exam 15 — Exam 2

Practice exam covering Weeks 8–13 (classes, inheritance, error handling) plus a little earlier material. Four short problems at the same level as the weekly work.

## What to build

1. `Car(make, model)` — remembers a make and a model.
   - `.describe()` returns them joined by a single space, e.g. `"Toyota Corolla"`.
   - Helpful example: `Car("Toyota", "Corolla").describe()` → `"Toyota Corolla"`
2. `Dog(Animal)` — a subclass of `Animal` whose `speak()` returns `"Woof!"`.
   - Helpful example: `Dog().speak()` → `"Woof!"`
3. `safe_divide(a, b)` — return `a` divided by `b`, or `None` when `b` is 0.
   - Helpful example: `safe_divide(6, 2)` → `3`; `safe_divide(1, 0)` → `None`
4. `add(a, b)` — return the sum of `a` and `b`.
   - Helpful example: `add(2, 3)` → `5`

## Helpful examples & notes

- Store values on `self` in `__init__`, then use them inside a method.
- A subclass (`class Dog(Animal)`) can override a method to change its behaviour.
- try / except handles an error instead of letting it crash the program.

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
