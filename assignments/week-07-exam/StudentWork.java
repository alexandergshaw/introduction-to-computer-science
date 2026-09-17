/*
 * Exam 07 — Exam 1
 * =================
 * Practice exam covering Weeks 0–6 (data types, control flow, methods, and data
 * structures). Three short problems at the same level as the weekly work.
 *
 * Write each method so it matches the description, then run TestAssignment.java
 * until all the tests pass.
 *
 * What to build:
 *   1. letterGrade(score)    -> the letter grade for a 0–100 score, using the
 *                              standard cutoffs: 90+ = A, 80+ = B, 70+ = C,
 *                              60+ = D, below 60 = F
 *   2. average(nums)         -> the average (mean) of the numbers in the array
 *   3. countPositives(nums)  -> how many numbers in the array are greater than 0
 *
 * Concepts you'll use:
 *   • if / else if checks run top to bottom and the first true one wins, so the
 *     order of your cutoffs matters.
 *   • nums.length is how many items an array holds; iterate to compute a sum.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return the letter grade for a numeric score (0–100) using the standard
     * cutoffs: 90+ = A, 80+ = B, 70+ = C, 60+ = D, anything below 60 = F.
     *
     * Example:
     *     letterGrade(95) -> "A"
     *     letterGrade(72) -> "C"
     *     letterGrade(40) -> "F"
     */
    public static String letterGrade(double score) {
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        if (score >= 60) return "D";
        return "F";
    }

    /**
     * Return the average (mean) of the numbers in nums.
     *
     * Example:
     *     average(new double[]{2, 4, 6}) -> 4.0
     */
    public static double average(double[] nums) {
        double sum = 0;
        for (double n : nums) sum += n;
        return sum / nums.length;
    }

    /**
     * Return how many numbers in nums are greater than 0.
     *
     * Example:
     *     countPositives(new double[]{-1, 2, 0, 5}) -> 2
     *     countPositives(new double[]{-3, -2})      -> 0
     */
    public static int countPositives(double[] nums) {
        int count = 0;
        for (double n : nums) if (n > 0) count++;
        return count;
    }
}
