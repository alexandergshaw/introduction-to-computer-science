/*
 * Assignment 08 — OOP: Classes
 * =============================
 * Week 8: writing your own classes with constructors and member functions.
 * Build three small classes so their objects behave as described below.
 *
 * Write the code so each object behaves correctly, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. Rectangle(width, height) — remembers its width and height.
 *        .area()  returns the rectangle's area.
 *   2. Square(side)             — remembers its side length.
 *        .area()  returns the square's area.
 *   3. Person(name)             — remembers a name.
 *        .greet() returns a short self-introduction of the form  Hi, I'm <name>
 *
 * Concepts you'll use:
 *   • A constructor runs automatically when an object is created, e.g. Rectangle(2, 3).
 *   • Member variables store values on the object; member functions read them.
 *
 * Tip: open test_assignment.cpp to see exactly how each object is created and used.
 */
#include <string>

/** A rectangle built from a width and a height. */
class Rectangle {
public:
    double width;
    double height;

    /** Remember this rectangle's width and height for later. */
    Rectangle(double width, double height) : width(width), height(height) {}

    /**
     * Return this rectangle's area.
     *
     * Example:
     *     Rectangle(3, 4).area() -> 12.0
     */
    double area() const {
        return width * height;
    }
};

/** A square built from one side length. */
class Square {
public:
    double side;

    /** Remember this square's side length for later. */
    explicit Square(double side) : side(side) {}

    /**
     * Return this square's area.
     *
     * Example:
     *     Square(5).area() -> 25.0
     */
    double area() const {
        return side * side;
    }
};

/** A person with a name. */
class Person {
public:
    std::string name;

    /** Remember this person's name for later. */
    explicit Person(const std::string& name) : name(name) {}

    /**
     * Return a short self-introduction of the form "Hi, I'm <name>".
     *
     * Example:
     *     Person("Ada").greet() -> "Hi, I'm Ada"
     */
    std::string greet() const {
        return "Hi, I'm " + name;
    }
};
