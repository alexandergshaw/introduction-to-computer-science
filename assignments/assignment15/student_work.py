"""
Student Work — Assignment 15: Supplemental Practice (Week 15)
=============================================================
Final supplemental practice module, running alongside Exam Practice 2.

──────────────────────────────────────────────────────
THE FINAL PUSH
──────────────────────────────────────────────────────
You're in the last few weeks of the course. This supplemental module
gives you one more round of hands-on practice before the final project.

Think of this as your "dress rehearsal" — a chance to combine
EVERYTHING you've learned into polished, well-structured code:

  ✅ Clean class hierarchies with meaningful inheritance
  ✅ Robust error handling that never lets the program crash unexpectedly
  ✅ File I/O that reads and writes data reliably
  ✅ Unit tests that verify your code works correctly
  ✅ Well-named functions with docstrings and type hints
  ✅ Git commits with clear, descriptive messages

──────────────────────────────────────────────────────
MINI PROJECT IDEAS FOR EXTRA PRACTICE
──────────────────────────────────────────────────────
If you have extra time and want to practice beyond the exercises,
try building one of these mini-projects from scratch:

  1. SIMPLE TO-DO LIST
     • A class TodoList with methods: add_task, complete_task,
       list_tasks, save_to_file, load_from_file.

  2. CONTACT BOOK
     • A class ContactBook with a dict of name → phone.
     • Methods: add_contact, remove_contact, search, save, load.
     • Handle FileNotFoundError when loading.

  3. QUIZ GAME
     • A list of questions (each a dict with "question" and "answer").
     • Ask each question, check the answer, track score.
     • Classes: Question, Quiz.

  4. SIMPLE BANK SYSTEM
     • Classes: BankAccount, SavingsAccount (inherits from BankAccount).
     • SavingsAccount adds an interest rate and apply_interest() method.
     • All operations log to a file.

These aren't required — they're just fun ways to get more reps!

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Complete each exercise applying all your skills.
3. When done, change MODULE_COMPLETED to True.

One more after this (the final project) and you're done! 🚀
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
