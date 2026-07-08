// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each function should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <string>
#include "student_work.cpp"

int main() {
    // testIsPalindrome
    assert(isPalindrome("racecar") == true);
    assert(isPalindrome("hello") == false);

    // testIsEven
    assert(isEven(4) == true);
    assert(isEven(7) == false);

    // testAbsolute
    assert(absolute(-5) == 5.0);
    assert(absolute(3) == 3.0);
    assert(absolute(0) == 0.0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
