"""
Student Work — Assignment 12: Advanced Unit Testing
====================================================
Week 11 introduced unit testing: what a test is, pytest, assert, testing
edge cases, pytest.raises(), and the Red → Green → Refactor cycle. Week 12
extends that foundation with the tools professionals use to write larger,
cleaner, more thorough test suites.

(You already practiced Git, branching, and pull requests back in Week 0's
setup, and you'll use them every time you submit — so this week we go
deeper on testing instead.)

Objectives for this week:

  ✓ Share setup with fixtures
  ✓ Run one test against many inputs with parametrization
  ✓ Isolate code from the outside world with mocking / monkeypatch
  ✓ Organize tests with the Arrange–Act–Assert pattern
  ✓ Measure how much of your code is exercised with coverage

──────────────────────────────────────────────────────
FIXTURES — REUSABLE SETUP
──────────────────────────────────────────────────────
A fixture builds something your tests need (a sample object, a temp file,
a database connection) so you don't repeat setup in every test.

    import pytest

    @pytest.fixture
    def sample_account():
        return Account(balance=100)

    def test_withdraw(sample_account):
        sample_account.withdraw(40)
        assert sample_account.balance == 60

pytest also ships built-in fixtures like `tmp_path` (a temporary folder)
for tests that touch the file system.

──────────────────────────────────────────────────────
PARAMETRIZATION — ONE TEST, MANY CASES
──────────────────────────────────────────────────────
Instead of copy-pasting a test for each input, run it against a table:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(a, b, expected):
        assert add(a, b) == expected

That's three independent test cases from one function.

──────────────────────────────────────────────────────
MOCKING / MONKEYPATCH — ISOLATING YOUR CODE
──────────────────────────────────────────────────────
A unit test should test YOUR code, not the network or the clock. Replace
real dependencies with stand-ins:

    def test_greeting(monkeypatch):
        monkeypatch.setattr("mymodule.now", lambda: "morning")
        assert greeting() == "Good morning"

`unittest.mock` (Mock, patch) does the same for objects and functions, and
lets you assert a dependency was called as expected.

──────────────────────────────────────────────────────
ARRANGE — ACT — ASSERT
──────────────────────────────────────────────────────
Structure each test in three clear phases:

    def test_deposit():
        account = Account(balance=0)   # Arrange
        account.deposit(50)            # Act
        assert account.balance == 50   # Assert

Each test should check ONE behavior and have a descriptive name.

──────────────────────────────────────────────────────
COVERAGE — WHAT DID THE TESTS ACTUALLY RUN?
──────────────────────────────────────────────────────
Coverage measures which lines your tests execute:

    pytest --cov=mymodule

High coverage doesn't guarantee correctness, but lines that are never run
are definitely untested. Aim to cover the important paths and edge cases.

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md and complete this module in Codespaces.
2. Practice: add a fixture and a parametrized test to a small function.
3. When finished, change MODULE_COMPLETED to True.

Strong tests are what let you change code without fear. 🧪
"""

# ─── Exercise solution ──────────────────────────────────────────────────────
# Exercise: clamp(n, low, high) keeps n inside the range low..high.
#   clamp(5, 0, 10) -> 5    clamp(-3, 0, 10) -> 0    clamp(99, 0, 10) -> 10
# Things to know:
#   • min(x, y) gives the SMALLER of two values; max(x, y) gives the LARGER.
# Hint (no spoilers): if n is too big, pull it down to high; if it's too
# small, lift it up to low. Combining min() and max() does both at once.
def clamp(n: float, low: float, high: float) -> float:
    """Constrain n to the inclusive range [low, high]."""
    # min(n, high) caps the top end; max(low, ...) lifts the bottom end.
    return max(low, min(n, high))
