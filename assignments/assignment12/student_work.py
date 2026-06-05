"""
Student Work — Assignment 12: Git and Branching
================================================
Week 12 covers Git — the version control system used by virtually
every professional software team on the planet.

──────────────────────────────────────────────────────
WHAT IS GIT?
──────────────────────────────────────────────────────
Git is a "version control system" — a tool that tracks changes to your
files over time. With Git you can:

  • See a complete history of every change ever made to your code
  • Go back to any previous version if you break something
  • Work on multiple features simultaneously without conflict
  • Collaborate with other developers on the same codebase

Think of Git as an unlimited "undo" button for your entire project,
with the ability to label and revisit any point in time.

──────────────────────────────────────────────────────
KEY GIT CONCEPTS
──────────────────────────────────────────────────────
  REPOSITORY (repo)
      A folder tracked by Git. Contains all your files AND the full
      history of every change. Your assignment repo is a Git repo.

  COMMIT
      A snapshot of your files at a specific point in time. Each commit
      has a unique ID (hash), a message, an author, and a timestamp.
      Commits are the "save points" in your project's history.

  BRANCH
      An independent line of development. The default branch is usually
      called "main" (or "master" in older repos). You can create new
      branches to work on features without affecting the main branch.

  MERGE
      Combining changes from one branch into another.

  REMOTE
      A copy of the repository hosted online (e.g., on GitHub). "origin"
      is the conventional name for the primary remote.

──────────────────────────────────────────────────────
ESSENTIAL GIT COMMANDS
──────────────────────────────────────────────────────
  git status
      → Shows which files have been changed, staged, or not tracked.
        Run this often — it's your "what's going on?" command.

  git add <file>
  git add .           (stage ALL changed files)
      → "Stages" files, marking them to be included in the next commit.

  git commit -m "your message here"
      → Creates a commit (snapshot) of your staged files.
        Write clear, descriptive messages! Bad: "fix". Good: "Fix crash
        when user enters empty string in login form".

  git log
  git log --oneline   (compact view)
      → Shows the commit history.

  git diff
      → Shows what has changed in your files since the last commit.

  git push origin main
      → Sends your local commits to the remote repository (GitHub).

  git pull origin main
      → Downloads the latest commits from GitHub to your local machine.

  git clone <url>
      → Creates a local copy of a remote repository.

──────────────────────────────────────────────────────
BRANCHING WORKFLOW
──────────────────────────────────────────────────────
  git branch                    # list all branches
  git branch feature-login      # create a new branch called feature-login
  git switch feature-login      # switch to that branch
  # (or: git checkout -b feature-login  — create AND switch in one command)

  # ... make changes, commit them ...

  git switch main               # go back to main
  git merge feature-login       # merge your feature into main

WHY BRANCH?
  • Work on a new feature without breaking the main branch
  • Multiple developers can work on different features simultaneously
  • Easy to abandon a failed experiment (just delete the branch)
  • Code review: others review a branch before it merges

──────────────────────────────────────────────────────
MERGE CONFLICTS
──────────────────────────────────────────────────────
A merge conflict happens when two branches changed the SAME line of
the SAME file differently. Git doesn't know which version to keep,
so it asks you.

Conflicted files will have markers like this:

    <<<<<<< HEAD
    your version of the line
    =======
    their version of the line
    >>>>>>> feature-branch

You manually edit the file to keep what you want, remove the markers,
save, then: git add <file> and git commit.

──────────────────────────────────────────────────────
GIT IN CODESPACES (NO TERMINAL NEEDED)
──────────────────────────────────────────────────────
In GitHub Codespaces you can do most Git operations using the
Source Control panel (the branching icon in the left sidebar):

  • View changed files
  • Stage files (click the + icon)
  • Write a commit message and click Commit
  • Sync (push/pull) with the cloud button
  • Create/switch branches from the status bar at the bottom

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Practice creating branches, making commits, and merging.
3. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "error: Your local changes would be overwritten by merge"
      → Commit or stash your local changes before pulling/merging.

  ✗ "CONFLICT — Automatic merge failed"
      → Open the conflicted file, resolve the markers, save,
        git add, then git commit.

  ✗ "fatal: not a git repository"
      → You're in the wrong folder. Navigate to your project root first.

Git is the #1 tool in every developer's toolkit. Invest time here —
it pays dividends for your entire career! 🌿
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all Git and branching exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
