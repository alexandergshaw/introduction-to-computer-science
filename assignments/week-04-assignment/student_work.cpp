/*
 * Assignment 04 — Functions and Modular Programming
 * ==================================================
 * Week 4: parameters, return values, and default parameter values.
 *
 * Write each function so it returns the described value, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. add(a, b, c=0.0)              -> the sum of the numbers; c is optional
 *   2. greet(name, greeting="Hello") -> a greeting of the form  <greeting>, <name>!
 *   3. triple(n)                     -> n multiplied by 3
 *
 * Concepts you'll use:
 *   • Writing  double c = 0.0  or  std::string greeting = "Hello"  in the
 *     function signature gives a parameter a default value.
 *   • The + operator joins two std::strings together.
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <string>

/**
 * Return the sum of a, b, and c. c is optional and defaults to 0.
 *
 * Example:
 *     add(2, 3)    -> 5.0
 *     add(2, 3, 4) -> 9.0
 */
double add(double a, double b, double c = 0.0) {
    return a + b + c;
}

/**
 * Return a greeting of the form "<greeting>, <name>!". greeting is optional
 * and defaults to "Hello".
 *
 * Example:
 *     greet("Sam")       -> "Hello, Sam!"
 *     greet("Sam", "Hi") -> "Hi, Sam!"
 */
std::string greet(const std::string& name, const std::string& greeting = "Hello") {
    return greeting + ", " + name + "!";
}

/**
 * Return n multiplied by 3.
 *
 * Example:
 *     triple(4) -> 12.0
 */
double triple(double n) {
    return n * 3;
}
