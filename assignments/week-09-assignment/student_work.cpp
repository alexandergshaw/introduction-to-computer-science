/*
 * Assignment 09 — Advanced OOP
 * =============================
 * Week 9: inheritance and overriding. There is one base class, Animal, and three
 * specific animals that each inherit from it. Every subclass overrides speak() so
 * it returns that animal's own sound.
 *
 * Write each subclass so its speak() returns the right sound, then compile and
 * run test_assignment.cpp until all the tests pass.
 *
 * What to build (each one is a subclass of Animal):
 *   1. Dog — speak() returns  Woof!
 *   2. Cat — speak() returns  Meow!
 *   3. Cow — speak() returns  Moo!
 *
 * Concepts you'll use:
 *   • Writing  class Dog : public Animal  means "a Dog is a kind of Animal".
 *   • Mark the base class method with  virtual  so subclasses can override it.
 *   • Use  override  in the subclass to confirm you are replacing the base method.
 *   • A pointer or reference to Animal can hold any subclass — that is polymorphism.
 *
 * Tip: open test_assignment.cpp to see the exact expected sounds.
 */
#include <string>

/** A generic animal. Each subclass overrides speak() with its own sound. */
class Animal {
public:
    virtual ~Animal() = default;

    /** The default sound; subclasses replace this with their own. */
    virtual std::string speak() const {
        return "...";
    }
};

class Dog : public Animal {
public:
    /** Return a dog's sound.  Example: Dog().speak() -> "Woof!" */
    std::string speak() const override {
        return "Woof!";
    }
};

class Cat : public Animal {
public:
    /** Return a cat's sound.  Example: Cat().speak() -> "Meow!" */
    std::string speak() const override {
        return "Meow!";
    }
};

class Cow : public Animal {
public:
    /** Return a cow's sound.  Example: Cow().speak() -> "Moo!" */
    std::string speak() const override {
        return "Moo!";
    }
};
