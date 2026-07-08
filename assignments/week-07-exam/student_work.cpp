/*
 * Exam 07 — Exam 1
 * =================
 * Practice exam covering Weeks 0–6 (data types, control flow, functions, and
 * data structures). Three short problems at the same level as the weekly work.
 *
 * Write each function so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. letterGrade(score)   -> the letter grade for a 0–100 score, using the
 *                             standard cutoffs: 90+ = A, 80+ = B, 70+ = C,
 *                             60+ = D, below 60 = F
 *   2. average(nums)        -> the average (mean) of the numbers in the vector
 *   3. countPositives(nums) -> how many numbers in the vector are greater than 0
 *
 * Concepts you'll use:
 *   • if / else if checks run top to bottom and the first true one wins, so the
 *     order of your cutoffs matters.
 *   • nums.size() is how many items a vector holds; std::accumulate sums them.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

/**
 * Return the letter grade for a numeric score (0–100) using the standard
 * cutoffs: 90+ = A, 80+ = B, 70+ = C, 60+ = D, anything below 60 = F.
 *
 * Example:
 *     letterGrade(95) -> "A"
 *     letterGrade(72) -> "C"
 *     letterGrade(40) -> "F"
 */
std::string letterGrade(double score) {
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
 *     average({2, 4, 6}) -> 4.0
 */
double average(const std::vector<double>& nums) {
    return std::accumulate(nums.begin(), nums.end(), 0.0) / nums.size();
}

/**
 * Return how many numbers in nums are greater than 0.
 *
 * Example:
 *     countPositives({-1, 2, 0, 5}) -> 2
 *     countPositives({-3, -2})      -> 0
 */
int countPositives(const std::vector<double>& nums) {
    return static_cast<int>(std::count_if(nums.begin(), nums.end(),
                                          [](double n) { return n > 0; }));
}
