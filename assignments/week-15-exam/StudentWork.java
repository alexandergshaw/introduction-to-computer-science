/*
 * Exam 15 — Exam 2
 * =================
 * Practice exam covering Weeks 8–13 (classes, inheritance, error handling) plus
 * a little earlier material. Four short problems at the same level as the weekly work.
 *
 * Write each one so it matches the description, then run TestAssignment.java until
 * all the tests pass.
 *
 * What to build:
 *   1. Car(make, model)  — remembers a make and a model.
 *        .describe() returns them joined by a single space, e.g.  Toyota Corolla
 *   2. Dog (extends Animal) — a subclass of Animal whose speak() returns  Woof!
 *   3. safeDivide(a, b)  -> a divided by b, or null when b is 0
 *   4. add(a, b)         -> the sum of a and b
 *
 * Tip: open TestAssignment.java to see the exact inputs and expected outputs.
 */
public class StudentWork {

    /** A car that can describe itself. */
    static class Car {
        private String make;
        private String model;

        /** Remember this car's make and model for later. */
        public Car(String make, String model) {
            this.make = make;
            this.model = model;
        }

        /**
         * Return the make and model joined by a single space.
         *
         * Example:
         *     new Car("Toyota", "Corolla").describe() -> "Toyota Corolla"
         */
        public String describe() {
            return make + " " + model;
        }
    }

    /** A generic animal. Subclasses override speak() with their own sound. */
    static class Animal {
        /** The default sound; subclasses replace this with their own. */
        public String speak() {
            return "...";
        }
    }

    /** A dog: a kind of Animal that overrides speak() with its own sound. */
    static class Dog extends Animal {
        /** Return a dog's sound.  Example: new Dog().speak() -> "Woof!" */
        @Override
        public String speak() {
            return "Woof!";
        }
    }

    /**
     * Return a divided by b. If b is 0, return null instead of crashing.
     *
     * Example:
     *     safeDivide(6, 2) -> 3.0
     *     safeDivide(1, 0) -> null
     */
    public static Double safeDivide(double a, double b) {
        if (b == 0) return null;
        return a / b;
    }

    /**
     * Return the sum of a and b.
     *
     * Example:
     *     add(2, 3) -> 5.0
     */
    public static double add(double a, double b) {
        return a + b;
    }
}
