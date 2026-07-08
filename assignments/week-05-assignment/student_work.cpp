/*
 * Assignment 05 — Data Structures
 * =================================
 * Week 5: vectors and sets, plus some handy standard-library functions.
 *
 * Write each function so it returns the described value, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. uniqueSorted(items) -> the values from items with duplicates removed,
 *                            arranged in ascending order
 *   2. total(nums)         -> the sum of all the numbers in the vector
 *   3. largest(nums)       -> the biggest number in the vector
 *
 * Concepts you'll use:
 *   • A  std::set<int>  drops duplicate values and keeps them sorted.
 *   • std::accumulate() from <numeric> adds up the values in a range.
 *   • std::max_element() from <algorithm> finds the largest element.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <numeric>
#include <set>
#include <vector>

/**
 * Return a vector of the unique values from items, sorted in ascending order.
 *
 * Example:
 *     uniqueSorted({3, 1, 3, 2}) -> {1, 2, 3}
 */
std::vector<int> uniqueSorted(const std::vector<int>& items) {
    std::set<int> s(items.begin(), items.end());
    return std::vector<int>(s.begin(), s.end());
}

/**
 * Return the sum of all the numbers in nums.
 *
 * Example:
 *     total({1, 2, 3}) -> 6
 */
int total(const std::vector<int>& nums) {
    return std::accumulate(nums.begin(), nums.end(), 0);
}

/**
 * Return the largest number in nums.
 *
 * Example:
 *     largest({4, 9, 2}) -> 9
 */
int largest(const std::vector<int>& nums) {
    return *std::max_element(nums.begin(), nums.end());
}
