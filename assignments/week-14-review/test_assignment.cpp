// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and function should do. Compile and run; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <optional>
#include <string>
#include "student_work.cpp"

int main() {
    // testBankAccount
    BankAccount acct;               // starts at 0
    assert(acct.balance == 0.0);
    acct.deposit(100);              // +100
    acct.withdraw(30);              // -30
    assert(acct.balance == 70.0);
    assert(BankAccount(50).balance == 50.0);  // opening balance

    // testSafeDivide
    assert(safeDivide(6, 2) == 3.0);
    assert(safeDivide(1, 0) == std::nullopt);

    // testIsPalindrome
    assert(isPalindrome("racecar") == true);
    assert(isPalindrome("hello") == false);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
