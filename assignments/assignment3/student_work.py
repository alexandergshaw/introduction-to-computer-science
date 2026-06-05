"""
Student Work — Assignment 3: Logic and Control Flow
====================================================
Week 3 is where things get really interesting. Programs aren't just
lists of instructions that run top-to-bottom — they make DECISIONS
and REPEAT actions. That's called "control flow."

──────────────────────────────────────────────────────
BOOLEANS AND COMPARISONS
──────────────────────────────────────────────────────
Control flow is driven by True/False conditions. Python gives you
several operators to compare values:

    ==   equal to                 5 == 5   → True
    !=   not equal to             5 != 3   → True
    >    greater than             10 > 7   → True
    <    less than                3 < 8    → True
    >=   greater than or equal    5 >= 5   → True
    <=   less than or equal       4 <= 6   → True

You can combine conditions with logical operators:

    and  — both conditions must be True
        age >= 18 and has_id == True   → True only if BOTH are true

    or   — at least one condition must be True
        is_admin or is_owner           → True if EITHER is true

    not  — flips True to False and vice versa
        not is_locked                  → True if is_locked is False

──────────────────────────────────────────────────────
IF / ELIF / ELSE — MAKING DECISIONS
──────────────────────────────────────────────────────
The if statement lets your program take different paths:

    grade = 88

    if grade >= 90:
        print("A")        # runs if grade is 90 or above
    elif grade >= 80:
        print("B")        # runs if grade is 80–89
    elif grade >= 70:
        print("C")        # runs if grade is 70–79
    else:
        print("Below C")  # runs if none of the above matched

KEY POINTS:
  • The colon (:) at the end of if/elif/else is required.
  • The code inside each block MUST be indented (4 spaces or 1 tab).
  • Python runs only the FIRST block whose condition is True, then skips
    the rest.
  • "elif" is short for "else if". You can have as many as you need.
  • "else" is a catch-all — it has no condition and runs when nothing
    else matched. It is optional.

──────────────────────────────────────────────────────
WHILE LOOPS — REPEATING WHILE A CONDITION IS TRUE
──────────────────────────────────────────────────────
    count = 0
    while count < 5:
        print(count)   # prints 0, 1, 2, 3, 4
        count += 1     # IMPORTANT: update the variable or you'll loop forever!

A "while" loop keeps running as long as its condition is True. Always
make sure something inside the loop eventually makes the condition False,
otherwise you'll create an infinite loop (press Ctrl+C to stop one).

──────────────────────────────────────────────────────
FOR LOOPS — ITERATING OVER A SEQUENCE
──────────────────────────────────────────────────────
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)   # prints each fruit on its own line

    # Using range() to repeat a specific number of times:
    for i in range(5):     # i goes 0, 1, 2, 3, 4
        print(i)

"for" loops are great when you know in advance how many times you want
to repeat something, or when you're going through items in a list.

──────────────────────────────────────────────────────
BREAK AND CONTINUE
──────────────────────────────────────────────────────
    break     — immediately exits the loop
    continue  — skips the rest of this iteration and jumps to the next

    for number in range(10):
        if number == 5:
            break          # stop the loop when we hit 5
        print(number)      # prints 0, 1, 2, 3, 4

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the detailed exercises.
2. Practice writing if/elif/else blocks and loops as directed.
3. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "IndentationError"
      → Python is strict about indentation. All lines inside an if block
        or loop must be indented by the same amount (4 spaces recommended).

  ✗ "SyntaxError: expected ':'"
      → You're missing the colon at the end of your if/elif/else/for/while line.

  ✗ Infinite loop (program never stops)
      → Your while loop condition never becomes False. Check that you're
        updating the variable the condition depends on inside the loop.

Control flow is the backbone of every program ever written. Master this
and you can do almost anything. Keep going! 🧠
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all logic and control flow exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
