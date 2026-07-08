/*
 * Assignment 09 — Advanced OOP
 * =============================
 * Week 9: inheritance and overriding. There is one base class, Animal, and three
 * specific animals that each inherit from it. Every subclass overrides speak() so
 * it returns that animal's own sound.
 *
 * Write each subclass so its speak() returns the right sound, then run
 * TestAssignment.java until all the tests pass.
 *
 * What to build (each one is a subclass of Animal):
 *   1. Dog — speak() returns  Woof!
 *   2. Cat — speak() returns  Meow!
 *   3. Cow — speak() returns  Moo!
 *
 * Concepts you'll use:
 *   • Writing  class Dog extends Animal  means "a Dog is a kind of Animal" and
 *     inherits everything Animal already has.
 *   • "Overriding" means defining speak() again inside the subclass so it behaves
 *     differently from the version in Animal.
 *   • The  @Override  annotation confirms you are replacing the parent's method.
 *
 * Tip: open TestAssignment.java to see the exact expected sounds.
 */
public class StudentWork {

    static class Animal {
        /** The default sound; subclasses replace this with their own. */
        public String speak() {
            return "...";
        }
    }

    static class Dog extends Animal {
        /** Return a dog's sound.  Example: new Dog().speak() -> "Woof!" */
        @Override
        public String speak() {
            return "Woof!";
        }
    }

    static class Cat extends Animal {
        /** Return a cat's sound.  Example: new Cat().speak() -> "Meow!" */
        @Override
        public String speak() {
            return "Meow!";
        }
    }

    static class Cow extends Animal {
        /** Return a cow's sound.  Example: new Cow().speak() -> "Moo!" */
        @Override
        public String speak() {
            return "Moo!";
        }
    }
}
