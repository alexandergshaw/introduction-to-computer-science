/*
 * Assignment 12 — Advanced Unit Testing
 * =======================================
 * Week 12: methods worth testing across many inputs (think parametrized tests).
 * Pay attention to the edge cases described below.
 *
 * Write each method so it matches the description, then run TestAssignment.java
 * until all the tests pass.
 *
 * What to build:
 *   1. clamp(n, low, high)   -> n if it is already within [low, high]; otherwise
 *                              the nearest boundary (low if too small, high if too big)
 *   2. inRange(n, low, high) -> true if n is between low and high, inclusive
 *   3. sign(n)               -> -1 if n is negative, 0 if it is zero, 1 if positive
 *
 * Concepts you'll use:
 *   • Math.min(x, y) returns the smaller of two values; Math.max(x, y) the larger.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return n limited to the inclusive range [low, high]: n itself if it's already
     * inside the range, otherwise the nearest boundary.
     *
     * Example:
     *     clamp(5, 0, 10)  -> 5.0
     *     clamp(15, 0, 10) -> 10.0
     *     clamp(-4, 0, 10) -> 0.0
     */
    public static double clamp(double n, double low, double high) {
        return Math.max(low, Math.min(n, high));
    }

    /**
     * Return true if n is between low and high (inclusive), otherwise false.
     *
     * Example:
     *     inRange(5, 0, 10)  -> true
     *     inRange(15, 0, 10) -> false
     */
    public static boolean inRange(double n, double low, double high) {
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
    public static int sign(double n) {
        if (n > 0) return 1;
        if (n < 0) return -1;
        return 0;
    }
}
