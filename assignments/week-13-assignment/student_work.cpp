/*
 * Assignment 13 — Best Practices
 * ================================
 * Week 13: clean, readable string helper functions. Three small problems.
 *
 * Write each function so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. formatFullName(first, last) -> "<first> <last>" as one string, with any
 *                                     extra spaces around each name removed
 *   2. initials(first, last)       -> the uppercase first letters, each followed
 *                                     by a dot, e.g. "Ada","Lovelace" -> "A.L."
 *   3. slugify(text)               -> a tidy, URL-friendly version of text:
 *                                     lowercase, trimmed, and with spaces turned
 *                                     into dashes
 *
 * Concepts you'll use:
 *   • Trim leading/trailing spaces by finding the first and last non-space character.
 *   • std::tolower() converts a single character to lowercase; apply it to every character.
 *   • std::string::replace() substitutes substrings in a string.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <cctype>
#include <string>

/** Remove leading and trailing whitespace from s. */
static std::string trim(const std::string& s) {
    size_t start = s.find_first_not_of(" \t\r\n");
    if (start == std::string::npos) return "";
    size_t end = s.find_last_not_of(" \t\r\n");
    return s.substr(start, end - start + 1);
}

/**
 * Return "<first> <last>" as a single string, with any extra spaces around
 * each name removed.
 *
 * Example:
 *     formatFullName("Ada", "Lovelace")      -> "Ada Lovelace"
 *     formatFullName("  Ada ", "Lovelace ")  -> "Ada Lovelace"
 */
std::string formatFullName(const std::string& first, const std::string& last) {
    return trim(first) + " " + trim(last);
}

/**
 * Return the uppercase initials, each followed by a dot.
 *
 * Example:
 *     initials("Ada", "Lovelace") -> "A.L."
 *     initials("grace", "hopper") -> "G.H."
 */
std::string initials(const std::string& first, const std::string& last) {
    std::string result;
    result += static_cast<char>(std::toupper(static_cast<unsigned char>(first[0])));
    result += '.';
    result += static_cast<char>(std::toupper(static_cast<unsigned char>(last[0])));
    result += '.';
    return result;
}

/**
 * Return a URL-friendly slug: lowercase, trimmed, with spaces turned into dashes.
 *
 * Example:
 *     slugify("  Hello World ") -> "hello-world"
 */
std::string slugify(const std::string& text) {
    std::string result = trim(text);
    std::transform(result.begin(), result.end(), result.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    std::string out;
    for (char c : result) out += (c == ' ' ? '-' : c);
    return out;
}
