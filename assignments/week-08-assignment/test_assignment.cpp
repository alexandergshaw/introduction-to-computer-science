// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and method should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <string>
#include "student_work.cpp"

int main() {
    // testRectangle
    assert(Rectangle(2, 3).area() == 6.0);
    assert(Rectangle(4, 5).area() == 20.0);

    // testSquare
    assert(Square(4).area() == 16.0);

    // testPerson
    assert(Person("Ada").greet() == "Hi, I'm Ada");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
