/*
 * Assignment 00 — Orientation
 * ============================
 * Your very first file. Three tiny warm-up functions to get you used to the loop
 * of "edit the code, then run the tests." Each one is a single line of code.
 *
 * How this works: every method below has a description (and usually an example)
 * telling you exactly what it should hand back. Write code so the behaviour
 * matches, then run TestAssignment.java from your IDE until all the tests pass.
 *
 * What to build:
 *   1. hello()             -> the exact text  Hello, world!
 *   2. favoriteLanguage()  -> the name of the programming language this file is written in
 *   3. doubleText(text)    -> the given text written out twice in a row
 *
 * Concepts you'll use:
 *   • A method hands a value back to whoever called it with the  return  keyword.
 *   • Text wrapped in double quotes is called a "String".
 *   • Two Strings can be combined into one longer String with the  +  operator.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /** Return the exact text: Hello, world! */
    public static String hello() {
        return "Hello, world!";
    }

    /** Return the name of the programming language this file is written in. */
    public static String favoriteLanguage() {
        return "Java";
    }

    /**
     * Return text written out twice in a row, with nothing in between.
     *
     * Example:
     *     doubleText("ab") -> "abab"
     */
    public static String doubleText(String text) {
        return text + text;
    }
}
