/*
 * Assignment 01 — C++ Basics
 * ===========================
 * Week 1: strings, simple functions, and string operations. Three short problems.
 *
 * Write each function so its behaviour matches the description, then compile and
 * run test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. greet(name)          -> a greeting addressed to name, e.g.  Hello, Sam!
 *   2. loud(text)           -> the same text, but in ALL CAPS
 *   3. addExcitement(text)  -> the same text with one exclamation point on the end
 *
 * Concepts you'll use:
 *   • The + operator joins two std::strings together.
 *   • std::toupper() converts a single character to uppercase; use it in a loop
 *     or with std::transform to uppercase the whole string.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <cctype>
#include <string>

/**
 * Return a greeting addressed to name.
 *
 * Example:
 *     greet("Sam") -> "Hello, Sam!"
 */
std::string greet(const std::string& name) {
    return "Hello, " + name + "!";
}

/**
 * Return an all-uppercase version of text.
 *
 * Example:
 *     loud("hi") -> "HI"
 */
std::string loud(std::string text) {
    std::transform(text.begin(), text.end(), text.begin(),
                   [](unsigned char c) { return std::toupper(c); });
    return text;
}

/**
 * Return text with a single exclamation point added to the end.
 *
 * Example:
 *     addExcitement("go") -> "go!"
 */
std::string addExcitement(const std::string& text) {
    return text + "!";
}
