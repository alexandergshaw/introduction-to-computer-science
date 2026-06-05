"""
Student Work — Assignment 1: Environment Setup
===============================================
Great job making it to Week 1! In this assignment you'll confirm that
your development environment is fully set up and working.

"Development environment" just means: the programs and tools you need
in order to write and run code. For this course that includes:
  • GitHub Codespaces (your cloud editor — no install needed!)
  • Python 3 (already available inside Codespaces)
  • The VS Code Testing panel (to run the automated tests)

WHAT TO DO
----------
1. Read through the INSTRUCTIONS.md file in this folder.
2. Follow the steps to verify your environment is working.
3. Once you've confirmed everything is running, change the line below
   from:
       MODULE_COMPLETED = False
   to:
       MODULE_COMPLETED = True

That single change tells the dashboard you've finished this module.

HOW THE COMPLETION FLAG WORKS
------------------------------
Python has a data type called "bool" (short for boolean). A boolean
can only ever be one of two values:

    True   ← means "yes" / "on" / "it's done"
    False  ← means "no"  / "off" / "not done yet"

These are NOT strings — do NOT put quotes around them. Correct:

    MODULE_COMPLETED = True    ✓
    MODULE_COMPLETED = False   ✓

Incorrect (these won't work the way you expect):

    MODULE_COMPLETED = "True"   ✗  (this is a string, not a boolean)
    MODULE_COMPLETED = true     ✗  (Python is case-sensitive; must be capital T)

WHAT module_status() DOES
--------------------------
The function below just returns whatever value MODULE_COMPLETED holds.
The test file calls this function to check whether you've completed
the module. You do NOT need to change the function — only change the
MODULE_COMPLETED value at the top.

    def module_status() -> bool:
        return MODULE_COMPLETED

The "-> bool" part is called a "type hint". It tells anyone reading
the code that this function returns a boolean. Python doesn't enforce
this at runtime, but it's good practice and makes code easier to read.

HOW THE TEST CHECKS YOUR WORK
-------------------------------
test_assignment.py contains two tests:

  1. test_module_completed_flag
       Checks that MODULE_COMPLETED is exactly True (not just truthy —
       it must be the Python boolean True).

  2. test_module_status_function_matches_flag
       Checks that module_status() returns the same value as
       MODULE_COMPLETED. Since the function just returns MODULE_COMPLETED,
       this will always pass as long as you haven't accidentally changed
       the function body.

TROUBLESHOOTING
---------------
  ✗ "assert module.MODULE_COMPLETED is True"
      → You haven't changed False to True yet, or you typed "True" with
        quotes (making it a string instead of a boolean).

  ✗ "assert module.module_status() is module.MODULE_COMPLETED"
      → You may have accidentally edited the module_status function.
        It should just say: return MODULE_COMPLETED

Nice work setting up your workspace. On to Week 2! 💻
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True once you've verified your environment is working.
#
#   Before:  MODULE_COMPLETED = False
#   After:   MODULE_COMPLETED = True
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
#
# You do NOT need to change anything below this line.
#
# This function returns the value of MODULE_COMPLETED so the test runner
# can check whether you've finished the module. It's a simple one-liner:
# whatever MODULE_COMPLETED is set to, that's what gets returned.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
