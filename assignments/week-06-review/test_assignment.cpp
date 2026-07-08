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
#include <vector>
#include "student_work.cpp"

int main() {
    // testClassify
    assert(classify(5) == "positive");
    assert(classify(-2) == "negative");
    assert(classify(0) == "zero");

    // testTotal
    assert(total({1, 2, 3}) == 6);

    // testGreet
    assert(greet("Sam") == "Hello, Sam!");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
