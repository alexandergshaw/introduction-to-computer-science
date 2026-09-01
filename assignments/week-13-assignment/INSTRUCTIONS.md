# Assignment 13 — Best Practices

Week 13: clean, readable string helpers. Three small problems.

## What to build

1. `format_full_name(first, last)` — return `"<first> <last>"` as a single string, with any extra spaces around each name removed.
   - Helpful example: `format_full_name("Ada", "Lovelace")` → `"Ada Lovelace"`; `format_full_name("  Ada ", "Lovelace ")` → `"Ada Lovelace"`
2. `initials(first, last)` — return the uppercase initials, each followed by a dot.
   - Helpful example: `initials("Ada", "Lovelace")` → `"A.L."`; `initials("grace", "hopper")` → `"G.H."`
3. `slugify(text)` — return a URL-friendly slug: lowercase, trimmed, with spaces turned into dashes.
   - Helpful example: `slugify("  Hello World ")` → `"hello-world"`

## Helpful examples & notes

- `.strip()` removes spaces from the start and end of a string; `.lower()` and `.upper()` change its case.
- `text[0]` is the first character of a string; `.replace(old, new)` swaps every occurrence of one substring for another.

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
