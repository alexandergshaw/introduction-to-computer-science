/*
 * Assignment 00 — Orientation
 * ============================
 * Your very first file. Three tiny warm-up functions to get you used to the loop
 * of "edit the code, then run the tests." Each one is a single line of code.
 *
 * How this works: every function below has a description (and usually an example)
 * telling you exactly what it should hand back. Write code so the behaviour
 * matches, then compile test_assignment.cpp and run it until all the tests pass.
 *
 * What to build:
 *   1. hello()             -> the exact text  Hello, world!
 *   2. favoriteLanguage()  -> the name of the programming language this file is written in
 *   3. doubleText(text)    -> the given text written out twice in a row
 *
 * Concepts you'll use:
 *   • A function hands a value back to whoever called it with the  return  keyword.
 *   • Text wrapped in double quotes is called a "string" (std::string in C++).
 *   • Two strings can be combined into one longer string with the  +  operator.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <string>

/** Return the exact text: Hello, world! */
std::string hello() {
    return "Hello, world!";
}

/** Return the name of the programming language this file is written in. */
std::string favoriteLanguage() {
    return "C++";
}

/**
 * Return text written out twice in a row, with nothing in between.
 *
 * Example:
 *     doubleText("ab") -> "abab"
 */
std::string doubleText(const std::string& text) {
    return text + text;
}
