/*
 * Assignment 04 — Functions and Modular Programming
 * ==================================================
 * Week 4: parameters, return values, and method overloading (Java's equivalent
 * of default parameter values). Three short problems.
 *
 * Write each method so it returns the described value, then run
 * TestAssignment.java until all the tests pass.
 *
 * What to build:
 *   1. add(a, b)              -> the sum of the two numbers
 *      add(a, b, c)           -> the sum of all three numbers
 *   2. greet(name)            -> a greeting of the form  Hello, <name>!
 *      greet(name, greeting)  -> a greeting of the form  <greeting>, <name>!
 *   3. triple(n)              -> n multiplied by 3
 *
 * Concepts you'll use:
 *   • Method overloading lets you define two methods with the same name but
 *     different parameters — Java calls the right one automatically.
 *   • String.format() or the + operator builds formatted strings.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return the sum of a and b (c defaults to 0).
     *
     * Example:
     *     add(2, 3) -> 5.0
     */
    public static double add(double a, double b) {
        return a + b;
    }

    /**
     * Return the sum of a, b, and c.
     *
     * Example:
     *     add(2, 3, 4) -> 9.0
     */
    public static double add(double a, double b, double c) {
        return a + b + c;
    }

    /**
     * Return a greeting of the form "Hello, <name>!" using the default greeting.
     *
     * Example:
     *     greet("Sam") -> "Hello, Sam!"
     */
    public static String greet(String name) {
        return "Hello, " + name + "!";
    }

    /**
     * Return a greeting of the form "<greeting>, <name>!".
     *
     * Example:
     *     greet("Sam", "Hi") -> "Hi, Sam!"
     */
    public static String greet(String name, String greeting) {
        return greeting + ", " + name + "!";
    }

    /**
     * Return n multiplied by 3.
     *
     * Example:
     *     triple(4) -> 12.0
     */
    public static double triple(double n) {
        return n * 3;
    }
}
