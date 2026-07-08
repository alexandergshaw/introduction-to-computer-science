/*
 * Exam 15 — Exam 2
 * =================
 * Practice exam covering Weeks 8–13 (classes, inheritance, error handling) plus
 * a little earlier material. Four short problems at the same level as the weekly work.
 *
 * Write each one so it matches the description, then compile and run
 * test_assignment.cpp until all the tests pass.
 *
 * What to build:
 *   1. Car(make, model)  — remembers a make and a model.
 *        .describe() returns them joined by a single space, e.g.  Toyota Corolla
 *   2. Dog (subclass of Animal) — overrides speak() to return  Woof!
 *   3. safeDivide(a, b)  -> a divided by b, or std::nullopt when b is 0
 *   4. add(a, b)         -> the sum of a and b
 *
 * Tip: open test_assignment.cpp to see the exact inputs and expected outputs.
 */
#include <optional>
#include <string>

/** A car that can describe itself. */
class Car {
public:
    std::string make;
    std::string model;

    /** Remember this car's make and model for later. */
    Car(const std::string& make, const std::string& model)
        : make(make), model(model) {}

    /**
     * Return the make and model joined by a single space.
     *
     * Example:
     *     Car("Toyota", "Corolla").describe() -> "Toyota Corolla"
     */
    std::string describe() const {
        return make + " " + model;
    }
};

/** A generic animal. Subclasses override speak() with their own sound. */
class Animal {
public:
    virtual ~Animal() = default;
    virtual std::string speak() const { return "..."; }
};

/** A dog: a kind of Animal that overrides speak() with its own sound. */
class Dog : public Animal {
public:
    /** Return a dog's sound.  Example: Dog().speak() -> "Woof!" */
    std::string speak() const override {
        return "Woof!";
    }
};

/**
 * Return a divided by b. If b is 0, return std::nullopt instead of crashing.
 *
 * Example:
 *     safeDivide(6, 2) -> 3.0
 *     safeDivide(1, 0) -> std::nullopt
 */
std::optional<double> safeDivide(double a, double b) {
    if (b == 0) return std::nullopt;
    return a / b;
}

/**
 * Return the sum of a and b.
 *
 * Example:
 *     add(2, 3) -> 5.0
 */
double add(double a, double b) {
    return a + b;
}
