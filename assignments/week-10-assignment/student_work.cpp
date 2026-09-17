/*
 * Assignment 10 — Error Handling and File I/O
 * ============================================
 * Week 10: using std::optional and defensive checks so your code reacts to
 * errors instead of crashing. Each function attempts a normal action and
 * returns a safe fallback if it fails.
 *
 * Write each function so it returns the right value in BOTH the success case and
 * the failure case, then compile and run test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. safeDivide(a, b)         -> a divided by b, or std::nullopt when b is 0
 *   2. toInt(text, defaultVal)  -> text converted to a whole number, or defaultVal
 *                                  when text isn't a valid number
 *   3. safeGet(items, index)    -> the item at that position in the vector, or
 *                                  std::nullopt when the index is out of range
 *
 * Concepts you'll use:
 *   • std::optional<T> (from <optional>) can hold a value or nothing (std::nullopt).
 *   • std::stoi() converts a string to an int but throws std::invalid_argument if
 *     the string isn't a number; wrap it in a try / catch.
 *   • Check whether an index is within  [0, items.size())  before using it.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <optional>
#include <string>
#include <vector>

/**
 * Return a divided by b. If b is 0, return std::nullopt instead of crashing.
 *
 * Example:
 *     safeDivide(6, 2) -> 3.0
 *     safeDivide(1, 0) -> std::nullopt
 */
std::optional<double> safeDivide(double a, double b) {
    if (b == 0) return std::nullopt;
    return a / b;
}

/**
 * Return text converted to an integer. If text isn't a valid whole number,
 * return defaultVal instead.
 *
 * Example:
 *     toInt("42", 0)   -> 42
 *     toInt("abc", 0)  -> 0
 *     toInt("abc", -1) -> -1
 */
int toInt(const std::string& text, int defaultVal = 0) {
    try {
        return std::stoi(text);
    } catch (...) {
        return defaultVal;
    }
}

/**
 * Return the item at position index in items. If index is out of range,
 * return std::nullopt.
 *
 * Example:
 *     safeGet({10, 20, 30}, 1) -> 20
 *     safeGet({10, 20, 30}, 9) -> std::nullopt
 */
std::optional<int> safeGet(const std::vector<int>& items, int index) {
    if (index < 0 || index >= static_cast<int>(items.size())) return std::nullopt;
    return items[index];
}
