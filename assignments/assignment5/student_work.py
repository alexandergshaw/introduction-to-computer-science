"""
Student Work — Assignment 5: Data Structures
=============================================
Week 5 introduces data structures — ways to organize and store
collections of data. Instead of having 100 separate variables, you
can group them together into one data structure.

──────────────────────────────────────────────────────
LISTS  [ ]  — ordered, changeable collections
──────────────────────────────────────────────────────
A list holds multiple values in a specific order. Each item has an
"index" (its position), starting at 0.

    fruits = ["apple", "banana", "cherry"]
    #          index 0   index 1   index 2

    print(fruits[0])     # apple       ← first item (index 0)
    print(fruits[-1])    # cherry      ← last item (negative index)
    print(fruits[1:3])   # ['banana', 'cherry']  ← slice

Common list operations:
    fruits.append("mango")       # add to the end
    fruits.insert(1, "blueberry") # insert at position 1
    fruits.remove("banana")      # remove first occurrence of "banana"
    fruits.pop()                 # remove and return the last item
    len(fruits)                  # number of items in the list
    "apple" in fruits            # True if "apple" is in the list

Iterating over a list:
    for fruit in fruits:
        print(fruit)

──────────────────────────────────────────────────────
DICTIONARIES  { }  — key-value pairs (like a real dictionary!)
──────────────────────────────────────────────────────
A dictionary maps "keys" to "values". Lookup is by key name, not
by position.

    student = {
        "name": "Maria Lopez",
        "age": 20,
        "gpa": 3.85
    }

    print(student["name"])   # Maria Lopez
    student["age"] = 21      # update a value
    student["major"] = "CS"  # add a new key-value pair
    del student["gpa"]       # delete a key-value pair

    # Safe lookup (returns None if key doesn't exist, no error):
    email = student.get("email")   # returns None

Iterating over a dictionary:
    for key, value in student.items():
        print(key, "→", value)

──────────────────────────────────────────────────────
TUPLES  ( )  — ordered, UNCHANGEABLE collections
──────────────────────────────────────────────────────
Tuples are like lists, but you can't modify them after creation.
Use them when data should stay constant (coordinates, RGB colors, etc.)

    point = (10, 25)
    x = point[0]   # 10
    y = point[1]   # 25

    # Tuple unpacking (very handy!):
    x, y = point   # x = 10, y = 25 at the same time

──────────────────────────────────────────────────────
SETS  { }  — unordered collections of UNIQUE values
──────────────────────────────────────────────────────
Sets automatically remove duplicates. Useful for membership testing.

    colors = {"red", "blue", "green", "red"}
    print(colors)   # {"red", "blue", "green"} — duplicate removed!

    "red" in colors   # True  ← very fast lookup
    colors.add("yellow")
    colors.discard("blue")

──────────────────────────────────────────────────────
CHOOSING THE RIGHT DATA STRUCTURE
──────────────────────────────────────────────────────
  Use a LIST when:
    • Order matters
    • You need to access items by position
    • You need to add/remove items

  Use a DICTIONARY when:
    • You need to look things up by name/key
    • You're storing related properties of one thing

  Use a TUPLE when:
    • Data should never change
    • You want to group a fixed number of related values

  Use a SET when:
    • You only care whether something IS in the collection
    • You want to eliminate duplicates automatically

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Practice creating, reading, and modifying each data structure.
3. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "IndexError: list index out of range"
      → You tried to access an index that doesn't exist. Remember
        the first index is 0 and the last is len(my_list) - 1.

  ✗ "KeyError: 'name'"
      → You tried to access a dictionary key that doesn't exist.
        Use .get("name") to return None instead of crashing.

  ✗ "TypeError: 'tuple' object does not support item assignment"
      → Tuples are immutable (cannot be changed). Create a new tuple
        or use a list instead.

Data structures are everywhere in programming. Master these four and
you can represent almost any real-world data. You've got this! 📦
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all data structure exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
