"""
Student Work — Exam 7: Exam Practice 1
=======================================
Week 7 is Exam Practice 1. This module helps you prepare for your
first exam by reviewing and applying everything from Weeks 0–6.

──────────────────────────────────────────────────────
WHAT THE EXAM COVERS
──────────────────────────────────────────────────────
Exam 1 tests your knowledge of:

  ✓ Git & GitHub workflow (Week 0): branching off main, commits, pull requests, merging
  ✓ Python basics (Week 1): running a file, print(), comments, reading errors
  ✓ Python data types (int, float, str, bool, None)
  ✓ Variable creation and assignment
  ✓ Comparison and logical operators
  ✓ Conditional statements (if / elif / else)
  ✓ Loops (while, for, range, break, continue)
  ✓ Functions (define, call, parameters, return values, scope)
  ✓ Data structures (list, dict, tuple, set)

──────────────────────────────────────────────────────
HOW TO PREPARE
──────────────────────────────────────────────────────
  1. RE-READ your student_work.py files from Weeks 1–6. The comments
     in each file contain the key concepts for that week.

  2. RE-DO exercises without looking at your previous solutions.
     If you can solve a problem fresh, you understand it.

  3. PRACTICE WRITING CODE BY HAND. On some exams you'll be asked
     to trace code (predict the output) without running it.

  4. TEST YOURSELF with these questions:
       • What is the output of: print(10 // 3) ?   (answer: 3)
       • What is the output of: print(10 % 3)  ?   (answer: 1)
       • What does range(2, 8, 2) produce?          (2, 4, 6)
       • What is the difference between = and ==?
       • What does .get() do on a dictionary?
       • What is the return value of a function with no return statement?

  5. KNOW YOUR ERRORS — understand what causes:
       • NameError  — using a variable before it's defined
       • IndexError — accessing a list index that doesn't exist
       • KeyError   — accessing a dictionary key that doesn't exist
       • TypeError  — wrong type (e.g., adding a string to an int)
       • SyntaxError — code that Python can't parse (missing colon, etc.)

──────────────────────────────────────────────────────
USEFUL PYTHON CHEAT SHEET
──────────────────────────────────────────────────────
  # Arithmetic
  +  -  *  /     # add, subtract, multiply, divide (float result)
  //             # integer division (floor)  10 // 3 = 3
  %              # modulo (remainder)        10 % 3  = 1
  **             # exponentiation            2 ** 8  = 256

  # String tricks
  len("hello")          # 5
  "hello".upper()       # "HELLO"
  "hello".startswith("h")  # True
  " hello ".strip()     # "hello"  (removes whitespace)
  ", ".join(["a","b"])  # "a, b"

  # List tricks
  sorted([3,1,2])       # [1, 2, 3]
  list.sort()           # sorts in place (no return value)
  list.reverse()        # reverses in place

  # Type conversion
  int("42")    # 42    (string → integer)
  str(42)      # "42"  (integer → string)
  float("3.14") # 3.14 (string → float)

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exam practice exercises.
2. Complete each exercise as described.
3. When all exercises are done, change MODULE_COMPLETED to True.

You've covered a lot of ground. Trust your preparation! 🎯
"""

# ─── Exercise solution ──────────────────────────────────────────────────────
# Exercise: letter_grade(score) turns a 0–100 score into a letter grade.
#   90+ -> "A", 80s -> "B", 70s -> "C", 60s -> "D", below 60 -> "F".
# Hint (no spoilers): check the HIGHEST cutoff first and work down. Each branch
# returns right away, so once one matches the rest are skipped automatically.
def letter_grade(score: float) -> str:
    """Return the letter grade for a numeric score (0–100)."""
    if score >= 90:      # 90 and above
        return "A"
    if score >= 80:      # 80–89 (we've already ruled out 90+)
        return "B"
    if score >= 70:      # 70–79
        return "C"
    if score >= 60:      # 60–69
        return "D"
    return "F"           # anything left is below 60
