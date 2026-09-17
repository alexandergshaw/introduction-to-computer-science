/*
 * Assignment 03 — Logic and Control Flow
 * =======================================
 * Week 3: comparisons and if / else if / else. Three short decisions.
 *
 * Write each method so it returns the described value, then run
 * TestAssignment.java until all the tests pass.
 *
 * What to build:
 *   1. classify(n)  -> "positive", "negative", or "zero" depending on n
 *   2. isEven(n)    -> true if n is even, otherwise false
 *   3. larger(a, b) -> whichever of the two numbers is bigger
 *
 * Concepts you'll use:
 *   • A comparison such as  n > 0  evaluates to true or false.
 *   • if / else if / else lets your code choose between different branches.
 *   • The  %  (modulo) operator gives the remainder left after a division.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return "positive" if n is greater than 0, "negative" if it is less than 0,
     * and "zero" if it is exactly 0.
     *
     * Example:
     *     classify(5)  -> "positive"
     *     classify(0)  -> "zero"
     */
    public static String classify(double n) {
        if (n > 0) return "positive";
        if (n < 0) return "negative";
        return "zero";
    }

    /**
     * Return true if the whole number n is even, otherwise false.
     *
     * Example:
     *     isEven(4) -> true
     *     isEven(7) -> false
     */
    public static boolean isEven(int n) {
        return n % 2 == 0;
    }

    /**
     * Return whichever of a and b is larger.
     *
     * Example:
     *     larger(3, 9) -> 9
     */
    public static double larger(double a, double b) {
        if (a > b) return a;
        return b;
    }
}
