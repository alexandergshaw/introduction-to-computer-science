"""
Assignment 04 — Functions and Modular Programming
=================================================
Week 4: parameters, return values, and DEFAULT parameter values.

Write each function so it returns the described value, then run
test_assignment.py until all the tests pass.

What to build:
  1. add(a, b, c=0)                -> the sum of the numbers; c is optional, so
                                      add(a, b) should still work
  2. greet(name, greeting="Hello") -> a greeting of the form  <greeting>, <name>!
                                      greeting is optional and defaults to "Hello"
  3. triple(n)                     -> n multiplied by 3

Concepts you'll use:
  • Writing  c=0  or  greeting="Hello"  in the signature gives a parameter a
    DEFAULT value, used automatically when the caller leaves that argument out.
  • An f-string (  f"..."  ) drops a value into text using  { }  (same as Week 1).

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def add(a: float, b: float, c: float = 0) -> float:
    """
    Return the sum of a, b, and c. c is optional and defaults to 0, so leaving
    it out simply adds the first two numbers.

    Example:
        add(2, 3)    -> 5
        add(2, 3, 4) -> 9
    """
    return a + b + c


def greet(name: str, greeting: str = "Hello") -> str:
    """
    Return a greeting of the form "<greeting>, <name>!". greeting is optional and
    defaults to "Hello".

    Example:
        greet("Sam")        -> "Hello, Sam!"
        greet("Sam", "Hi")  -> "Hi, Sam!"
    """
    return f"{greeting}, {name}!"


def triple(n: float) -> float:
    """
    Return n multiplied by 3.

    Example:
        triple(4) -> 12
    """
    return n * 3
