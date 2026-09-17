/*
 * Review 06 — Review 1
 * =====================
 * A mixed review of Weeks 0–5: control flow, data structures, and methods — one
 * short problem from each area. You've written this kind of code before; if you
 * get stuck, revisit the earlier week noted in parentheses.
 *
 * Write each method so it matches the description, then run TestAssignment.java
 * until all the tests pass.
 *
 * What to build:
 *   1. classify(n) -> "positive", "negative", or "zero" depending on n   (Week 3)
 *   2. total(nums) -> the sum of all the numbers in the array             (Week 5)
 *   3. greet(name) -> a greeting of the form  Hello, <name>!              (Week 1)
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
     * Return the sum of all the numbers in nums.
     *
     * Example:
     *     total(new int[]{1, 2, 3}) -> 6
     */
    public static int total(int[] nums) {
        int sum = 0;
        for (int n : nums) sum += n;
        return sum;
    }

    /**
     * Return a greeting of the form "Hello, <name>!".
     *
     * Example:
     *     greet("Sam") -> "Hello, Sam!"
     */
    public static String greet(String name) {
        return "Hello, " + name + "!";
    }
}
