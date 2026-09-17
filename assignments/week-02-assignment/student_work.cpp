/*
 * Assignment 02 — Variables and Deployment
 * =========================================
 * Week 2: variables and arithmetic. Three short calculations.
 *
 * Write each function so it returns the described value, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. rectangleArea(width, height) -> the area of that rectangle
 *   2. square(n)                    -> n squared (n multiplied by itself)
 *   3. average(a, b)                -> the average (mean) of the two numbers
 *
 * Concepts you'll use:
 *   • C++'s math operators:  +  -  *  /   (* multiplies, / divides).
 *   • Parentheses control the order of operations.
 *   • Use  double  for numbers that can have a decimal part.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */

/**
 * Return the area of a rectangle with the given width and height.
 *
 * Example:
 *     rectangleArea(3, 4) -> 12.0
 */
double rectangleArea(double width, double height) {
    return width * height;
}

/**
 * Return n squared (the result of multiplying n by itself).
 *
 * Example:
 *     square(4) -> 16.0
 */
double square(double n) {
    return n * n;
}

/**
 * Return the average (mean) of the two numbers a and b.
 *
 * Example:
 *     average(4, 6) -> 5.0
 */
double average(double a, double b) {
    return (a + b) / 2;
}
