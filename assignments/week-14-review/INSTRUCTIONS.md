# Review 14 — Review 2

A mixed review of Weeks 8–13: a class, error handling, and a testing-friendly function. You've built each of these kinds of things before.

## What to build

1. `BankAccount(balance=0)` — a class that remembers a balance (starting at 0 when no opening balance is given). It has:
   - `.deposit(amount)` — increases the balance by `amount`
   - `.withdraw(amount)` — decreases the balance by `amount`
2. `safe_divide(a, b)` — return `a` divided by `b`, or `None` when `b` is 0. *(error handling)*
   - Helpful example: `safe_divide(6, 2)` → `3`; `safe_divide(1, 0)` → `None`
3. `is_palindrome(s)` — return `True` if `s` reads the same backwards, ignoring capitalisation. *(testing)*
   - Helpful example: `is_palindrome("racecar")` → `True`; `is_palindrome("hello")` → `False`

## Helpful examples & notes

- A class keeps its state on `self` (here, `self.balance`) and its methods change that state.
- try / except handles an error (such as dividing by zero) instead of crashing.
- A string's `.lower()` copy and its reverse (the `[::-1]` slice) help compare a string with itself.

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
