/*
 * Assignment 12 — Advanced Unit Testing
 * =======================================
 * Week 12: functions worth testing across many inputs (think parametrized tests).
 * Pay attention to the edge cases described below.
 *
 * Write each function so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. clamp(n, low, high)   -> n if it is already within [low, high]; otherwise
 *                              the nearest boundary (low if too small, high if too big)
 *   2. inRange(n, low, high) -> true if n is between low and high, inclusive
 *   3. sign(n)               -> -1 if n is negative, 0 if it is zero, 1 if positive
 *
 * Concepts you'll use:
 *   • std::min(x, y) returns the smaller of two values; std::max(x, y) the larger.
 *   • C++ allows chained comparisons written as separate conditions with &&.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>

/**
 * Return n limited to the inclusive range [low, high]: n itself if it's already
 * inside the range, otherwise the nearest boundary.
 *
 * Example:
 *     clamp(5, 0, 10)  -> 5.0
 *     clamp(15, 0, 10) -> 10.0
 *     clamp(-4, 0, 10) -> 0.0
 */
double clamp(double n, double low, double high) {
    return std::max(low, std::min(n, high));
}

/**
 * Return true if n is between low and high (inclusive), otherwise false.
 *
 * Example:
 *     inRange(5, 0, 10)  -> true
 *     inRange(15, 0, 10) -> false
 */
bool inRange(double n, double low, double high) {
    return n >= low && n <= high;
}

/**
 * Return 1 if n is positive, -1 if n is negative, and 0 if n is zero.
 *
 * Example:
 *     sign(-3) -> -1
 *     sign(0)  -> 0
 *     sign(8)  -> 1
 */
int sign(double n) {
    if (n > 0) return 1;
    if (n < 0) return -1;
    return 0;
}
