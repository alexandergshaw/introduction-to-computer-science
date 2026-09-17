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
    // testAdd
    assert(add(2, 3) == 5.0);       // c defaults to 0
    assert(add(2, 3, 4) == 9.0);    // all three added

    // testGreet
    assert(greet("Sam") == "Hello, Sam!");          // default greeting
    assert(greet("Sam", "Hi") == "Hi, Sam!");       // custom greeting

    // testTriple
    assert(triple(5) == 15.0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
