// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each function should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
#include "student_work.cpp"

int main() {
    // testSafeDivide
    assert(safeDivide(6, 2) == 3.0);           // normal division
    assert(safeDivide(1, 0) == std::nullopt);   // divide-by-zero handled

    // testToInt
    assert(toInt("42", 0) == 42);              // a valid number
    assert(toInt("abc", 0) == 0);              // not a number -> default 0
    assert(toInt("abc", -1) == -1);            // custom default

    // testSafeGet
    assert(safeGet({10, 20, 30}, 1) == 20);           // valid index
    assert(safeGet({10, 20, 30}, 9) == std::nullopt);  // out of range -> nullopt

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
