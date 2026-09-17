/*
 * Review 14 — Review 2
 * =====================
 * A mixed review of Weeks 8–13: a class, error handling, and a testing-friendly
 * function. You've built each of these kinds of things before.
 *
 * Write each one so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. BankAccount    — a class that remembers a balance (starting at 0
 *      when no opening balance is given). It has:
 *        .deposit(amount)  — increases the balance by amount
 *        .withdraw(amount) — decreases the balance by amount
 *   2. safeDivide(a, b) -> a divided by b, or std::nullopt when b is 0
 *   3. isPalindrome(s)  -> true if s reads the same backwards,
 *                          ignoring capitalisation
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <algorithm>
#include <cctype>
#include <optional>
#include <string>

/** A minimal bank account that tracks a balance. */
class BankAccount {
public:
    double balance;

    /** Create an account with zero balance. */
    BankAccount() : balance(0) {}

    /** Create an account with the given opening balance. */
    explicit BankAccount(double balance) : balance(balance) {}

    /** Increase the account's balance by amount. */
    void deposit(double amount) {
        balance += amount;
    }

    /** Decrease the account's balance by amount. */
    void withdraw(double amount) {
        balance -= amount;
    }
};

/**
 * Return a divided by b. If b is 0, return std::nullopt instead of crashing.
 *
 * Example:
 *     safeDivide(6, 2) -> 3.0
 *     safeDivide(1, 0) -> std::nullopt
 */
std::optional<double> safeDivide(double a, double b) {
    if (b == 0) return std::nullopt;
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
bool isPalindrome(std::string s) {
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    std::string reversed = s;
    std::reverse(reversed.begin(), reversed.end());
    return s == reversed;
}
