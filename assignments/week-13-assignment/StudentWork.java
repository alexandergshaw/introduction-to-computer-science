/*
 * Assignment 13 — Best Practices
 * ================================
 * Week 13: clean, readable String helper methods. Three small problems.
 *
 * Write each method so it matches the description, then run TestAssignment.java
 * until all the tests pass.
 *
 * What to build:
 *   1. formatFullName(first, last) -> "<first> <last>" as one String, with any
 *                                     extra spaces around each name removed
 *   2. initials(first, last)       -> the uppercase first letters, each followed
 *                                     by a dot, e.g. "Ada","Lovelace" -> "A.L."
 *   3. slugify(text)               -> a tidy, URL-friendly version of text:
 *                                     lowercase, trimmed, and with spaces turned
 *                                     into dashes
 *
 * Concepts you'll use:
 *   • .strip() / .trim() removes spaces from the start and end of a String.
 *   • .toLowerCase() and .toUpperCase() change its case.
 *   • text.charAt(0) is the first character of a String.
 *   • .replace(old, new) swaps every occurrence of one substring for another.
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /**
     * Return "<first> <last>" as a single String, with any extra spaces around
     * each name removed.
     *
     * Example:
     *     formatFullName("Ada", "Lovelace")      -> "Ada Lovelace"
     *     formatFullName("  Ada ", "Lovelace ")  -> "Ada Lovelace"
     */
    public static String formatFullName(String first, String last) {
        return first.strip() + " " + last.strip();
    }

    /**
     * Return the uppercase initials, each followed by a dot.
     *
     * Example:
     *     initials("Ada", "Lovelace") -> "A.L."
     *     initials("grace", "hopper") -> "G.H."
     */
    public static String initials(String first, String last) {
        return Character.toUpperCase(first.charAt(0)) + "." +
               Character.toUpperCase(last.charAt(0)) + ".";
    }

    /**
     * Return a URL-friendly slug: lowercase, trimmed, with spaces turned into dashes.
     *
     * Example:
     *     slugify("  Hello World ") -> "hello-world"
     */
    public static String slugify(String text) {
        return text.strip().toLowerCase().replace(" ", "-");
    }
}
