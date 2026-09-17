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
    // testClamp
    assert(clamp(5, 0, 10) == 5.0);     // already inside the range
    assert(clamp(-3, 0, 10) == 0.0);    // too low  -> snaps up to 0
    assert(clamp(99, 0, 10) == 10.0);   // too high -> snaps down to 10

    // testInRange
    assert(inRange(5, 0, 10) == true);
    assert(inRange(15, 0, 10) == false);

    // testSign
    assert(sign(7) == 1);
    assert(sign(-7) == -1);
    assert(sign(0) == 0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
