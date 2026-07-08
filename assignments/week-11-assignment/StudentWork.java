/*
 * Assignment 11 — Unit Testing
 * =============================
 * Week 11: small, predictable methods that are easy to test, including their
 * edge cases. Build the three methods described below.
 *
 * Write each method so it matches the description, then run TestAssignment.java
 * until all the tests pass.
 *
 * What to build:
 *   1. isPalindrome(s) -> true if s reads the same forwards and backwards,
 *                        ignoring capitalisation; otherwise false
 *   2. isEven(n)       -> true if the whole number n is even; otherwise false
 *   3. absolute(n)     -> the size of n with no negative sign (its distance from 0)
 *
 * Concepts you'll use:
 *   • A String has a .toLowerCase() method (a lowercase copy), useful for ignoring
 *     capitalisation.
 *   • Use a StringBuilder or loop to reverse a string.
 *   • The  %  (modulo) operator gives the remainder left after a division.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return true if s reads the same forwards and backwards, ignoring
     * capitalisation; otherwise false.
     *
     * Example:
     *     isPalindrome("racecar") -> true
     *     isPalindrome("hello")   -> false
     */
    public static boolean isPalindrome(String s) {
        String cleaned = s.toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();
        return cleaned.equals(reversed);
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
     * Return the absolute value of n — its distance from 0, which is never negative.
     *
     * Example:
     *     absolute(-3) -> 3.0
     *     absolute(5)  -> 5.0
     */
    public static double absolute(double n) {
        if (n < 0) return -n;
        return n;
    }
}
