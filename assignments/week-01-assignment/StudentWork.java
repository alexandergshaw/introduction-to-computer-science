/*
 * Assignment 01 — Java Basics
 * ============================
 * Week 1: Strings, simple methods, and String formatting. Three short problems.
 *
 * Write each method so its behaviour matches the description, then run
 * TestAssignment.java until all the tests pass.
 *
 * What to build:
 *   1. greet(name)           -> a greeting addressed to name, e.g.  Hello, Sam!
 *   2. loud(text)            -> the same text, but in ALL CAPS
 *   3. addExcitement(text)   -> the same text with one exclamation point on the end
 *
 * Concepts you'll use:
 *   • String.format() or the + operator lets you build a string from parts.
 *   • Strings have a .toUpperCase() method that returns an all-uppercase copy.
 *   • The + operator joins two Strings together.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return a greeting addressed to name.
     *
     * Example:
     *     greet("Sam") -> "Hello, Sam!"
     */
    public static String greet(String name) {
        return "Hello, " + name + "!";
    }

    /**
     * Return an all-uppercase version of text.
     *
     * Example:
     *     loud("hi") -> "HI"
     */
    public static String loud(String text) {
        return text.toUpperCase();
    }

    /**
     * Return text with a single exclamation point added to the end.
     *
     * Example:
     *     addExcitement("go") -> "go!"
     */
    public static String addExcitement(String text) {
        return text + "!";
    }
}
