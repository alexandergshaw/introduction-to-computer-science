"""
Student Work — Assignment 4: Functions and Modular Programming
==============================================================
Week 4 is all about functions — the single most important tool for
writing clean, organized, and reusable code.

──────────────────────────────────────────────────────
WHAT IS A FUNCTION?
──────────────────────────────────────────────────────
A function is a named, reusable block of code that performs a specific
task. Instead of copying the same code over and over, you write it once
in a function and call it whenever you need it.

    # Define the function once
    def greet(name):
        print("Hello, " + name + "!")

    # Call it as many times as you want
    greet("Maria")    # prints: Hello, Maria!
    greet("Jordan")   # prints: Hello, Jordan!

──────────────────────────────────────────────────────
ANATOMY OF A FUNCTION
──────────────────────────────────────────────────────
    def function_name(parameter1, parameter2):
        'A short description of what this function does.'
        # ... your code here ...
        return some_value

  def          — the keyword that starts a function definition
  function_name — you choose this; use snake_case (lowercase + underscores)
  parameters    — inputs the function expects (can have none, one, or many)
  '...'         — a docstring: a description of the function (optional but recommended)
  return        — sends a value back to wherever the function was called

──────────────────────────────────────────────────────
PARAMETERS VS ARGUMENTS
──────────────────────────────────────────────────────
These terms are often used interchangeably, but technically:

  PARAMETER — the variable name in the function definition
      def add(a, b):   # 'a' and 'b' are PARAMETERS
          return a + b

  ARGUMENT — the actual value you pass when calling the function
      add(3, 5)        # 3 and 5 are ARGUMENTS

──────────────────────────────────────────────────────
RETURN VALUES
──────────────────────────────────────────────────────
A function can "return" a value back to the caller:

    def square(number):
        return number * number

    result = square(4)   # result is now 16
    print(result)        # prints: 16

If a function has no return statement (or just "return" with nothing
after it), it returns None.

──────────────────────────────────────────────────────
DEFAULT PARAMETER VALUES
──────────────────────────────────────────────────────
You can give parameters a default value so they're optional:

    def greet(name, greeting="Hello"):
        print(greeting + ", " + name + "!")

    greet("Maria")            # Hello, Maria!
    greet("Jordan", "Hey")    # Hey, Jordan!

Parameters with defaults must come AFTER parameters without defaults.

──────────────────────────────────────────────────────
WHY MODULAR PROGRAMMING?
──────────────────────────────────────────────────────
"Modular programming" means breaking your program into small, focused
functions — each doing one thing well. This has huge benefits:

  ✓ Reusability     — write once, call anywhere
  ✓ Readability     — code reads like steps in a recipe
  ✓ Testability     — easy to test one small function at a time
  ✓ Maintainability — fix a bug in one place instead of everywhere

A good rule of thumb: if a function is longer than ~20 lines, consider
splitting it into smaller helper functions.

──────────────────────────────────────────────────────
SCOPE — WHERE VARIABLES LIVE
──────────────────────────────────────────────────────
Variables created INSIDE a function only exist inside that function.
This is called "local scope":

    def my_function():
        x = 10        # x only exists inside my_function
        print(x)      # works fine

    print(x)          # NameError! x doesn't exist out here

Variables created OUTSIDE functions (at the top level of your file)
are "global" and can be read from inside functions.

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Write the functions described there.
3. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "NameError: name 'x' is not defined"
      → You're trying to use a variable that doesn't exist in the
        current scope. Check where you defined it.

  ✗ "TypeError: function() takes 2 positional arguments but 3 were given"
      → You called the function with more arguments than it has parameters.

  ✗ Function returns None when you expect a value
      → You forgot to add a "return" statement inside your function.

Functions are the building blocks of all good software. You're thinking
like a real programmer now. Onwards! 🏗️
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all function-writing exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
