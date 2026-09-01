# Assignment 08 — OOP: Classes

Week 8: writing your own classes with `__init__`, `self`, and methods. Build three small classes so their objects behave as described below.

## What to build

1. `Rectangle(width, height)` — remembers its width and height.
   - `.area()` returns the rectangle's area.
   - Helpful example: `Rectangle(3, 4).area()` → `12`
2. `Square(side)` — remembers its side length.
   - `.area()` returns the square's area.
   - Helpful example: `Square(5).area()` → `25`
3. `Person(name)` — remembers a name.
   - `.greet()` returns a short self-introduction of the form `"Hi, I'm <name>"`.
   - Helpful example: `Person("Ada").greet()` → `"Hi, I'm Ada"`

## Helpful examples & notes

- `__init__` runs automatically when an object is created, e.g. `Rectangle(2, 3)`.
- `self` refers to THIS particular object; you store values on it by writing something like `self.width = width`.
- A method can read the values saved on `self` to work out its answer.

> Tip: open `test_assignment.py` to see exactly how each object is created and used.

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
