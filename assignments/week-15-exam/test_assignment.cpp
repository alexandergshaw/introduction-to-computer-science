// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and function should do. Compile and run; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <optional>
#include <string>
#include "student_work.cpp"

int main() {
    // testCar
    assert(Car("Toyota", "Corolla").describe() == "Toyota Corolla");

    // testDog
    Dog dog;
    assert(dog.speak() == "Woof!");
    Animal* dogAsAnimal = &dog;    // inheritance
    assert(dogAsAnimal->speak() == "Woof!");

    // testSafeDivide
    assert(safeDivide(6, 2) == 3.0);
    assert(safeDivide(1, 0) == std::nullopt);

    // testAdd
    assert(add(2, 3) == 5.0);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
