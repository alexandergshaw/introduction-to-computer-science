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
    // testClassify
    assert(classify(5) == "positive");
    assert(classify(-2) == "negative");
    assert(classify(0) == "zero");

    // testIsEven
    assert(isEven(4) == true);
    assert(isEven(7) == false);

    // testLarger
    assert(larger(3, 9) == 9.0);
    assert(larger(8, 2) == 8.0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
