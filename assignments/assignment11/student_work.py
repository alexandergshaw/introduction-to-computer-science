"""
Student Work — Assignment 11: Unit Testing
===========================================
Week 11 is all about unit testing — one of the most important
professional skills in software development.

──────────────────────────────────────────────────────
WHAT IS A UNIT TEST?
──────────────────────────────────────────────────────
A unit test is a small piece of code that automatically checks
whether ONE specific "unit" of your code (usually a single function)
behaves correctly.

Instead of manually running your code and eyeballing the output,
unit tests do that checking for you — automatically, every time —
so you can catch bugs immediately.

You've actually been using tests this whole semester! Every
test_assignment.py file in this course was written to verify your
student_work.py automatically.

──────────────────────────────────────────────────────
WHY WRITE TESTS?
──────────────────────────────────────────────────────
  ✓ Catch bugs immediately when they're introduced
  ✓ Prevent regressions (old bugs coming back when you add new code)
  ✓ Document expected behavior (tests ARE documentation)
  ✓ Give you confidence to change code without fear of breaking things
  ✓ Required at virtually every professional software job

The general rule: if you write code that matters, you write tests for it.

──────────────────────────────────────────────────────
PYTEST — THE TESTING FRAMEWORK WE USE
──────────────────────────────────────────────────────
pytest is the most popular Python testing framework. It finds and
runs any function whose name starts with "test_" in any file whose
name starts with "test_".

WRITING A TEST:
    # File: test_calculator.py
    from calculator import add, multiply   # import the functions to test

    def test_add_two_positive_numbers():
        assert add(2, 3) == 5

    def test_add_negative_numbers():
        assert add(-1, -1) == -2

    def test_multiply_by_zero():
        assert multiply(5, 0) == 0

THE assert STATEMENT:
    assert <condition>, "optional message if it fails"

  If the condition is True  → test PASSES silently
  If the condition is False → test FAILS with an AssertionError

  Examples:
    assert 2 + 2 == 4             # passes
    assert len("hello") == 5      # passes
    assert "foo" in ["foo","bar"] # passes
    assert 2 + 2 == 5             # FAILS — AssertionError!

──────────────────────────────────────────────────────
WHAT MAKES A GOOD UNIT TEST?
──────────────────────────────────────────────────────
  1. Tests ONE thing — each test function checks exactly one behavior.
  2. Has a descriptive name — test_add_returns_correct_sum is great;
     test1 is useless.
  3. Is independent — tests shouldn't depend on each other or share state.
  4. Tests EDGE CASES, not just the happy path:
       • What happens with an empty list?
       • What happens with 0?
       • What happens with negative numbers?
       • What happens with a very large number?

──────────────────────────────────────────────────────
TESTING EXCEPTIONS WITH pytest.raises
──────────────────────────────────────────────────────
Sometimes you WANT your code to raise an exception. Test that:

    import pytest

    def test_divide_by_zero_raises():
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)   # this SHOULD raise ZeroDivisionError

    def test_invalid_age_raises_value_error():
        with pytest.raises(ValueError):
            set_age(-5)     # should raise ValueError for negative age

──────────────────────────────────────────────────────
TEST-DRIVEN DEVELOPMENT (TDD)
──────────────────────────────────────────────────────
TDD is a development approach where you write the TEST first, before
you write the actual code. The cycle is:

    1. 🔴 RED   — write a failing test for the feature you want
    2. 🟢 GREEN  — write the minimum code to make the test pass
    3. 🔵 REFACTOR — clean up the code while keeping tests green

TDD might seem backwards at first, but it forces you to think about
what your code should DO before you think about HOW to do it.

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific testing exercises.
2. Write the functions AND the tests for them.
3. Run the tests from the Testing panel to confirm they pass.
4. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "ModuleNotFoundError: No module named 'calculator'"
      → Make sure your import statement matches the actual filename.

  ✗ "FAILED test_add_two_numbers - AssertionError: assert 4 == 5"
      → Your function returned the wrong value. Debug your function,
        not the test!

  ✗ No tests collected / "0 tests ran"
      → Make sure your test file starts with "test_" and each test
        function name starts with "test_".

Writing tests is a superpower. You'll never regret it. 🧪
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all unit testing exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
