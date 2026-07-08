// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each function should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <vector>
#include "student_work.cpp"

int main() {
    // testUniqueSorted
    assert((uniqueSorted({3, 1, 3, 2}) == std::vector<int>{1, 2, 3}));
    assert((uniqueSorted({}) == std::vector<int>{}));

    // testTotal
    assert(total({1, 2, 3}) == 6);
    assert(total({}) == 0);

    // testLargest
    assert(largest({3, 9, 2}) == 9);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
