// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testCar() {
        assertEquals("Toyota Corolla",
                     new StudentWork.Car("Toyota", "Corolla").describe());
    }

    @Test
    void testDog() {
        StudentWork.Dog dog = new StudentWork.Dog();
        assertEquals("Woof!", dog.speak());
        assertInstanceOf(StudentWork.Animal.class, dog);   // inheritance
    }

    @Test
    void testSafeDivide() {
        assertEquals(3.0, StudentWork.safeDivide(6, 2));
        assertNull(StudentWork.safeDivide(1, 0));
    }

    @Test
    void testAdd() {
        assertEquals(5.0, StudentWork.add(2, 3));
    }
}
