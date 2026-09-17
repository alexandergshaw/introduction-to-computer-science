/*
 * Assignment 11 — Unit Testing
 * =============================
 * Week 11: small, predictable functions that are easy to test, including their
 * edge cases. Build the three functions described below.
 *
 * Write each function so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. isPalindrome(s) -> true if s reads the same forwards and backwards,
 *                        ignoring capitalisation; otherwise false
 *   2. isEven(n)       -> true if the whole number n is even; otherwise false
 *   3. absolute(n)     -> the size of n with no negative sign (its distance from 0)
 *
 * Concepts you'll use:
 *   • std::tolower() converts a character to lowercase; apply it to every character.
 *   • std::reverse() from <algorithm> reverses a string in place.
 *   • The  %  (modulo) operator gives the remainder left after a division.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <cctype>
#include <string>

/**
 * Return true if s reads the same forwards and backwards, ignoring
 * capitalisation; otherwise false.
 *
 * Example:
 *     isPalindrome("racecar") -> true
 *     isPalindrome("hello")   -> false
 */
bool isPalindrome(std::string s) {
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    std::string reversed = s;
    std::reverse(reversed.begin(), reversed.end());
    return s == reversed;
}

/**
 * Return true if the whole number n is even, otherwise false.
 *
 * Example:
 *     isEven(4) -> true
 *     isEven(7) -> false
 */
bool isEven(int n) {
    return n % 2 == 0;
}

/**
 * Return the absolute value of n — its distance from 0, which is never negative.
 *
 * Example:
 *     absolute(-3) -> 3.0
 *     absolute(5)  -> 5.0
 */
double absolute(double n) {
    if (n < 0) return -n;
    return n;
}
