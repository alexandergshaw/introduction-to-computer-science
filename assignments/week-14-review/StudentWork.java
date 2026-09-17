/*
 * Review 14 — Review 2
 * =====================
 * A mixed review of Weeks 8–13: a class, error handling, and a testing-friendly
 * method. You've built each of these kinds of things before.
 *
 * Write each one so it matches the description, then run TestAssignment.java until
 * all the tests pass.
 *
 * What to build:
 *   1. BankAccount(balance)  — a class that remembers a balance (starting at 0
 *      when no opening balance is given). It has:
 *        .deposit(amount)  — increases the balance by amount
 *        .withdraw(amount) — decreases the balance by amount
 *   2. safeDivide(a, b) -> a divided by b, or null when b is 0  (error handling)
 *   3. isPalindrome(s)  -> true if s reads the same backwards,
 *                          ignoring capitalisation              (testing)
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    static class BankAccount {
        public double balance;

        /** Create an account with zero balance. */
        public BankAccount() {
            this.balance = 0;
        }

        /** Create an account with the given opening balance. */
        public BankAccount(double balance) {
            this.balance = balance;
        }

        /** Increase the account's balance by amount. */
        public void deposit(double amount) {
            balance += amount;
        }

        /** Decrease the account's balance by amount. */
        public void withdraw(double amount) {
            balance -= amount;
        }
    }

    /**
     * Return a divided by b. If b is 0, return null instead of crashing.
     *
     * Example:
     *     safeDivide(6, 2) -> 3.0
     *     safeDivide(1, 0) -> null
     */
    public static Double safeDivide(double a, double b) {
        if (b == 0) return null;
        return a / b;
    }

    /**
     * Return true if s reads the same forwards and backwards, ignoring
     * capitalisation; otherwise false.
     *
     * Example:
     *     isPalindrome("racecar") -> true
     *     isPalindrome("hello")   -> false
     */
    public static boolean isPalindrome(String s) {
        String cleaned = s.toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();
        return cleaned.equals(reversed);
    }
}
