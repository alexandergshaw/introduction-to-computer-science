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
    // testFormatFullName
    assert(formatFullName("Ada", "Lovelace") == "Ada Lovelace");
    assert(formatFullName("  Ada ", "Lovelace ") == "Ada Lovelace");

    // testInitials
    assert(initials("Ada", "Lovelace") == "A.L.");
    assert(initials("grace", "hopper") == "G.H.");

    // testSlugify
    assert(slugify("  Hello World ") == "hello-world");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
