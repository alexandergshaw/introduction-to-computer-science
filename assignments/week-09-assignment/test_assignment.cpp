// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class should do. Compile and run this file; aim for no failures.
//
// Compile:  g++ -std=c++17 -o test_assignment test_assignment.cpp
// Run:      ./test_assignment
// ─────────────────────────────────────────────────────────────────────────────
#include <cassert>
#include <iostream>
#include <memory>
#include <string>
#include "student_work.cpp"

int main() {
    // testDog
    Dog dog;
    assert(dog.speak() == "Woof!");
    // a Dog is still an Animal (polymorphism)
    Animal* dogAsAnimal = &dog;
    assert(dogAsAnimal->speak() == "Woof!");

    // testCat
    Cat cat;
    assert(cat.speak() == "Meow!");
    Animal* catAsAnimal = &cat;
    assert(catAsAnimal->speak() == "Meow!");

    // testCow
    Cow cow;
    assert(cow.speak() == "Moo!");
    Animal* cowAsAnimal = &cow;
    assert(cowAsAnimal->speak() == "Moo!");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
