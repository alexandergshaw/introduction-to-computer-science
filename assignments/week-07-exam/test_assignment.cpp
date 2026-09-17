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
    // testLetterGrade
    assert(letterGrade(95) == "A");
    assert(letterGrade(85) == "B");
    assert(letterGrade(72) == "C");
    assert(letterGrade(65) == "D");
    assert(letterGrade(40) == "F");

    // testAverage
    assert(average({2, 4, 6}) == 4.0);

    // testCountPositives
    assert(countPositives({-1, 2, 0, 5}) == 2);
    assert(countPositives({-3, -2}) == 0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
