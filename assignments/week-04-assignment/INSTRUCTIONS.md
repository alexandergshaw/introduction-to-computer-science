# Assignment 04 — Functions and Modular Programming

Week 4: parameters, return values, and DEFAULT parameter values.

## What to build

1. `add(a, b, c=0)` — return the sum of `a`, `b`, and `c`. `c` is optional and defaults to 0, so leaving it out simply adds the first two numbers.
   - Helpful example: `add(2, 3)` → `5`; `add(2, 3, 4)` → `9`
2. `greet(name, greeting="Hello")` — return a greeting of the form `"<greeting>, <name>!"`. `greeting` is optional and defaults to `"Hello"`.
   - Helpful example: `greet("Sam")` → `"Hello, Sam!"`; `greet("Sam", "Hi")` → `"Hi, Sam!"`
3. `triple(n)` — return `n` multiplied by 3.
   - Helpful example: `triple(4)` → `12`

## Helpful examples & notes

- Writing `c=0` or `greeting="Hello"` in the signature gives a parameter a DEFAULT value, used automatically when the caller leaves that argument out.
- An f-string (`f"..."`) drops a value into text using `{ }` (same as Week 1).

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
