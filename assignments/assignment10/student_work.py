"""
Student Work — Assignment 10: Error Handling and File I/O
==========================================================
Week 10 covers two essential real-world skills:
  1. ERROR HANDLING — writing code that gracefully deals with problems
  2. FILE I/O — reading from and writing to files on disk

──────────────────────────────────────────────────────
PART 1: ERROR HANDLING WITH TRY / EXCEPT
──────────────────────────────────────────────────────
When something goes wrong in Python, it raises an "exception" — an
error that, if unhandled, crashes your program. try/except lets you
catch those errors and respond to them gracefully.

BASIC SYNTAX:
    try:
        # code that might fail goes here
        result = 10 / 0
    except ZeroDivisionError:
        # this runs if a ZeroDivisionError occurs
        print("You can't divide by zero!")

MULTIPLE EXCEPT CLAUSES — handle different error types differently:
    try:
        number = int(input("Enter a number: "))
        result = 100 / number
    except ValueError:
        print("That's not a valid integer.")
    except ZeroDivisionError:
        print("Can't divide by zero.")

CATCHING ANY EXCEPTION with a generic handler (use sparingly):
    except Exception as e:
        print(f"Something went wrong: {e}")

ELSE — runs only if no exception occurred:
    try:
        value = int("42")
    except ValueError:
        print("Not a number!")
    else:
        print(f"Successfully converted: {value}")  # runs if try succeeded

FINALLY — ALWAYS runs, whether or not an exception occurred.
           Perfect for cleanup (like closing files):
    try:
        file = open("data.txt")
        data = file.read()
    except FileNotFoundError:
        print("File not found.")
    finally:
        file.close()   # always close the file!

──────────────────────────────────────────────────────
COMMON EXCEPTION TYPES
──────────────────────────────────────────────────────
  ValueError      — right type, wrong value: int("hello")
  TypeError       — wrong type entirely: "5" + 5
  ZeroDivisionError — dividing by zero: 10 / 0
  IndexError      — list index out of range: [1,2,3][10]
  KeyError        — dict key doesn't exist: {"a":1}["b"]
  FileNotFoundError — file doesn't exist when you try to open it
  AttributeError  — object doesn't have that attribute/method
  NameError       — variable used before it was defined

──────────────────────────────────────────────────────
RAISING YOUR OWN EXCEPTIONS
──────────────────────────────────────────────────────
You can raise exceptions intentionally to enforce rules:

    def set_age(age):
        if age < 0:
            raise ValueError(f"Age cannot be negative, got {age}")
        self.age = age

──────────────────────────────────────────────────────
PART 2: FILE INPUT / OUTPUT
──────────────────────────────────────────────────────
Python makes it easy to read and write text files.

READING A FILE:
    # Method 1: read entire file as one string
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

    # Method 2: read line by line (good for large files)
    with open("notes.txt", "r") as file:
        for line in file:
            print(line.strip())   # .strip() removes the newline \n

    # Method 3: read all lines into a list
    with open("notes.txt", "r") as file:
        lines = file.readlines()   # ['line1\n', 'line2\n', ...]

WRITING A FILE:
    # "w" mode overwrites the file (creates it if it doesn't exist)
    with open("output.txt", "w") as file:
        file.write("Hello, file!\n")
        file.write("Second line.\n")

    # "a" mode appends to an existing file (doesn't erase it)
    with open("output.txt", "a") as file:
        file.write("Added this later.\n")

THE "with" STATEMENT — WHY USE IT?
------------------------------------
The "with open(...) as file:" pattern automatically CLOSES the file
when the block ends, even if an error occurs. This is the safest,
most Pythonic way to work with files. Always prefer it over manually
calling file.open() and file.close().

FILE MODES:
  "r"  — read only (default); error if file doesn't exist
  "w"  — write (creates new or overwrites existing)
  "a"  — append (adds to end of existing file)
  "x"  — exclusive create (error if file already exists)
  "rb" — read binary (for images, PDFs, etc.)
  "wb" — write binary

──────────────────────────────────────────────────────
COMBINING BOTH: SAFE FILE READING
──────────────────────────────────────────────────────
    def read_file_safely(filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: '{filename}' does not exist.")
            return None
        except PermissionError:
            print(f"Error: no permission to read '{filename}'.")
            return None

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Write code that handles errors and reads/writes files.
3. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "FileNotFoundError"
      → The file path is wrong, or you're running the script from the
        wrong directory. Check that the file exists where you expect it.

  ✗ "IndentationError" inside try/except
      → Make sure all code inside try: and except: is indented.

  ✗ File is written but with missing or double newlines
      → Remember that file.write() doesn't add a newline automatically.
        Add "\n" at the end of each line you write.

Error handling is what separates amateur code from professional code.
You're writing real software now! 🛡️
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all error handling and file I/O exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
