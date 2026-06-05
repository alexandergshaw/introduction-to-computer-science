"""
Student Work — Assignment 14: Supplemental Practice (Week 14)
=============================================================
Additional practice module for Week 14, running alongside Review 2.

──────────────────────────────────────────────────────
WHAT THIS MODULE IS FOR
──────────────────────────────────────────────────────
This supplemental module provides extra coding practice on the topics
covered in Weeks 8–13. Use it to:

  • Reinforce concepts that felt shaky during review
  • Get more hands-on experience before Exam Practice 2
  • Explore real-world applications of what you've learned

──────────────────────────────────────────────────────
PUTTING IT ALL TOGETHER
──────────────────────────────────────────────────────
By now you have a powerful toolkit. Here's how the skills connect:

  CLASSES + ERROR HANDLING:
    class TemperatureConverter:
        def celsius_to_fahrenheit(self, celsius: float) -> float:
            if not isinstance(celsius, (int, float)):
                raise TypeError("Temperature must be a number.")
            return (celsius * 9 / 5) + 32

  CLASSES + FILE I/O:
    class StudentLog:
        def save(self, filename: str) -> None:
            with open(filename, "w") as f:
                f.write(str(self.data))

  CLASSES + UNIT TESTING:
    # test_temperature.py
    def test_celsius_to_fahrenheit_freezing():
        converter = TemperatureConverter()
        assert converter.celsius_to_fahrenheit(0) == 32

  CLASSES + INHERITANCE + BEST PRACTICES:
    class Shape:
        'Abstract base for all shapes.'
        def area(self) -> float:
            raise NotImplementedError

    class Rectangle(Shape):
        'A rectangle with width and height.'
        def __init__(self, width: float, height: float) -> None:
            self.width = width
            self.height = height

        def area(self) -> float:
            'Return the area of the rectangle.'
            return self.width * self.height

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Apply your full skillset as directed.
3. When done, change MODULE_COMPLETED to True.

You're in the home stretch. Stay focused! 🏁
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
