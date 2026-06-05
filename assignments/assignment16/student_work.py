"""
Student Work — Assignment 16: Final Project
============================================
Welcome to the last module of Introduction to Computer Science.
This is your Final Project — a chance to bring EVERYTHING you've
learned this semester together into one cohesive piece of work.

──────────────────────────────────────────────────────
WHAT THE FINAL PROJECT IS
──────────────────────────────────────────────────────
The final project is an open-ended Python program that demonstrates
mastery of the core skills from this course. The goal is to build
something that:

  • Solves a real (or realistic) problem
  • Shows off your ability to write clean, organized code
  • Uses the key concepts from the semester

Your instructor's INSTRUCTIONS.md will specify the exact requirements.
The information below is meant to help you plan, structure, and approach
a significant coding project.

──────────────────────────────────────────────────────
RECOMMENDED PROJECT STRUCTURE
──────────────────────────────────────────────────────
A well-organized Python project typically has:

    my_project/
    ├── main.py              ← entry point (run this to start the program)
    ├── student_work.py      ← this file (completion flag lives here)
    ├── models.py            ← your classes / data models
    ├── utils.py             ← helper functions
    ├── data.py              ← constants, sample data, config
    ├── test_models.py       ← unit tests for models.py
    └── test_utils.py        ← unit tests for utils.py

You don't have to use every file — adapt this to your project's needs.

──────────────────────────────────────────────────────
PROJECT PLANNING PROCESS (DO THIS FIRST)
──────────────────────────────────────────────────────
Before writing a single line of code, spend time planning:

  STEP 1 — DEFINE THE PROBLEM
    What does your program DO? Write a one-paragraph description.
    Who would use it? What problem does it solve?

  STEP 2 — IDENTIFY THE DATA
    What information does your program track?
    How should it be stored? (lists? dicts? objects?)

  STEP 3 — DESIGN YOUR CLASSES
    What are the "things" in your program?
    What data (attributes) does each thing have?
    What can each thing DO (methods)?
    Are there relationships? (inheritance? composition?)

  STEP 4 — PLAN YOUR FUNCTIONS
    What utility functions do you need?
    What operations are performed repeatedly?
    (Remember DRY — don't repeat yourself!)

  STEP 5 — PLAN YOUR TESTS
    What's the most critical functionality?
    What edge cases might break things?
    Write a list of tests BEFORE you write the code.

  STEP 6 — BUILD IT INCREMENTALLY
    Build and test one small piece at a time.
    Don't try to write the entire program at once.
    Get each part working before moving to the next.

──────────────────────────────────────────────────────
FINAL PROJECT CHECKLIST
──────────────────────────────────────────────────────
Use this checklist as you work:

  FUNCTIONALITY
    □ The program does what it's supposed to do
    □ Input validation and error handling are in place
    □ Edge cases are handled (empty input, invalid data, etc.)

  CODE QUALITY
    □ Classes are used appropriately
    □ Functions are small and focused (one job each)
    □ Variable and function names are descriptive
    □ No copy-pasted code (DRY principle followed)

  DOCUMENTATION
    □ Module-level docstring at the top of each .py file
    □ Docstrings on every class and every function
    □ Inline comments explain any non-obvious logic

  TESTING
    □ Unit tests exist for core functions and methods
    □ Tests cover both normal cases AND edge cases
    □ All tests pass

  GIT
    □ Multiple commits with clear, descriptive messages
    □ No massive "everything at once" commits
    □ Branch used for development, merged into main

  STYLE
    □ Follows PEP 8 (snake_case, 4-space indentation, etc.)
    □ Lines are kept under 79 characters where possible

──────────────────────────────────────────────────────
TIPS FOR SUCCESS
──────────────────────────────────────────────────────
  1. START EARLY. This is the most time-intensive assignment of the
     semester. Don't leave it to the last day.

  2. BUILD IN STAGES. Get a working "v1" that does the basics, THEN
     add polish and extra features. Working simple > broken complex.

  3. COMMIT OFTEN. Every time something works, commit it. That way
     if you break something, you can always go back.

  4. TEST AS YOU GO. Don't wait until the end to test. Write a test
     for each function right after you write the function.

  5. ASK FOR HELP EARLY. If you're stuck for more than 30 minutes,
     reach out. Getting unstuck quickly is a skill too.

  6. READ THE INSTRUCTIONS CAREFULLY. More than once. Make sure you're
     building exactly what's asked.

  7. HAVE FUN WITH IT. The best projects come from genuine curiosity.
     If you can, pick a topic that actually interests you.

──────────────────────────────────────────────────────
COMPLETING THIS MODULE
──────────────────────────────────────────────────────
This is the only module where the INSTRUCTIONS.md will tell you
exactly what "complete" means for the final project. Follow those
instructions carefully, then change MODULE_COMPLETED to True.

You have learned so much this semester. Variables, loops, functions,
data structures, OOP, error handling, file I/O, testing, Git, and
best practices. That is a LOT. Be proud of how far you've come.

Now go build something awesome. This is your moment! 🌟
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing your final project.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
