/*
 * Assignment 08 — OOP: Classes
 * =============================
 * Week 8: writing your own classes with constructors, fields, and methods.
 * Build three small classes so their objects behave as described below.
 *
 * Write the code so each object behaves correctly, then run TestAssignment.java
 * until all the tests pass.
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
 *   • A constructor runs automatically when an object is created, e.g. new Rectangle(2, 3).
 *   • "this" refers to THIS particular object; store values with  this.width = width .
 *   • A method can read the fields saved on the object to work out its answer.
 *
 * Tip: open TestAssignment.java to see exactly how each object is created and used.
 */
public class StudentWork {

    static class Rectangle {
        private double width;
        private double height;

        /** Remember this rectangle's width and height for later. */
        public Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        /**
         * Return this rectangle's area.
         *
         * Example:
         *     new Rectangle(3, 4).area() -> 12.0
         */
        public double area() {
            return width * height;
        }
    }

    static class Square {
        private double side;

        /** Remember this square's side length for later. */
        public Square(double side) {
            this.side = side;
        }

        /**
         * Return this square's area.
         *
         * Example:
         *     new Square(5).area() -> 25.0
         */
        public double area() {
            return side * side;
        }
    }

    static class Person {
        private String name;

        /** Remember this person's name for later. */
        public Person(String name) {
            this.name = name;
        }

        /**
         * Return a short self-introduction of the form "Hi, I'm <name>".
         *
         * Example:
         *     new Person("Ada").greet() -> "Hi, I'm Ada"
         */
        public String greet() {
            return "Hi, I'm " + name;
        }
    }
}
