/*
 * Assignment 05 — Data Structures
 * =================================
 * Week 5: arrays and lists, plus some handy utility methods.
 *
 * Write each method so it returns the described value, then run
 * TestAssignment.java until all the tests pass.
 *
 * What to build:
 *   1. uniqueSorted(items) -> the values from items with duplicates removed,
 *                            arranged in ascending order
 *   2. total(nums)         -> the sum of all the numbers in the array
 *   3. largest(nums)       -> the biggest number in the array
 *
 * Concepts you'll use:
 *   • A  TreeSet<Integer>  drops duplicate values and keeps them sorted.
 *   • Iterate over an array with a  for-each  loop.
 *   • Return an  int[]  array from a collection with  toArray().
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
import java.util.Arrays;
import java.util.TreeSet;

public class StudentWork {

    /**
     * Return an array of the unique values from items, sorted in ascending order.
     *
     * Example:
     *     uniqueSorted(new int[]{3, 1, 3, 2}) -> {1, 2, 3}
     */
    public static int[] uniqueSorted(int[] items) {
        TreeSet<Integer> set = new TreeSet<>();
        for (int item : items) set.add(item);
        int[] result = new int[set.size()];
        int i = 0;
        for (int v : set) result[i++] = v;
        return result;
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
     * Return the largest number in nums.
     *
     * Example:
     *     largest(new int[]{4, 9, 2}) -> 9
     */
    public static int largest(int[] nums) {
        int max = nums[0];
        for (int n : nums) if (n > max) max = n;
        return max;
    }
}
