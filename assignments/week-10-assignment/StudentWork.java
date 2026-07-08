/*
 * Assignment 10 — Error Handling and File I/O
 * ============================================
 * Week 10: using try / catch so your code reacts to errors instead of crashing.
 * Each method attempts a normal action and returns a safe fallback if it fails.
 *
 * Write each method so it returns the right value in BOTH the success case and
 * the failure case, then run TestAssignment.java until all the tests pass.
 *
 * What to build:
 *   1. safeDivide(a, b)          -> a divided by b, or null when b is 0
 *   2. toInt(text, defaultValue) -> text converted to a whole number, or
 *                                   defaultValue when text isn't a valid number
 *   3. safeGet(items, index)     -> the item at that position in the array, or
 *                                   null when the index is out of range
 *
 * Concepts you'll use:
 *   • Code that might fail goes in a  try { }  block; a  catch (SomeException e) { }
 *     block runs only when that specific exception is thrown.
 *   • Dividing by 0 with integers throws ArithmeticException in Java; use double
 *     and check manually instead.
 *   • Integer.parseInt("abc") throws NumberFormatException.
 *   • Accessing an array with a bad index throws ArrayIndexOutOfBoundsException.
 *   • Return  null  (using the boxed Double type) to signal "no result".
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return a divided by b. If b is 0, return null instead of crashing.
     *
     * Example:
     *     safeDivide(6, 2) -> 3.0
     *     safeDivide(1, 0) -> null
     */
    public static Double safeDivide(double a, double b) {
        if (b == 0) return null;
        return a / b;
    }

    /**
     * Return text converted to an integer. If text isn't a valid whole number,
     * return defaultValue instead.
     *
     * Example:
     *     toInt("42", 0)   -> 42
     *     toInt("abc", 0)  -> 0
     *     toInt("abc", -1) -> -1
     */
    public static int toInt(String text, int defaultValue) {
        try {
            return Integer.parseInt(text);
        } catch (NumberFormatException e) {
            return defaultValue;
        }
    }

    /**
     * Return the item at position index in items. If index is out of range,
     * return null.
     *
     * Example:
     *     safeGet(new int[]{10, 20, 30}, 1) -> 20
     *     safeGet(new int[]{10, 20, 30}, 9) -> null
     */
    public static Integer safeGet(int[] items, int index) {
        try {
            return items[index];
        } catch (ArrayIndexOutOfBoundsException e) {
            return null;
        }
    }
}
