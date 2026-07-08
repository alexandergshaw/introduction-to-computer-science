// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each function should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include "student_work.cpp"

int main() {
    // testRectangleArea
    assert(rectangleArea(3, 4) == 12.0);
    assert(rectangleArea(5, 5) == 25.0);

    // testSquare
    assert(square(4) == 16.0);
    assert(square(10) == 100.0);

    // testAverage
    assert(average(4, 6) == 5.0);
    assert(average(10, 0) == 5.0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
