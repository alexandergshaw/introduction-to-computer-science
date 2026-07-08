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
    // testGreet
    assert(greet("Sam") == "Hello, Sam!");
    assert(greet("Ada") == "Hello, Ada!");

    // testLoud
    assert(loud("hi") == "HI");
    assert(loud("Wow") == "WOW");

    // testAddExcitement
    assert(addExcitement("go") == "go!");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
