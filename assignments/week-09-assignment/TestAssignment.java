// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testDog() {
        StudentWork.Dog dog = new StudentWork.Dog();
        assertEquals("Woof!", dog.speak());
        assertInstanceOf(StudentWork.Animal.class, dog);  // a Dog is still an Animal
    }

    @Test
    void testCat() {
        StudentWork.Cat cat = new StudentWork.Cat();
        assertEquals("Meow!", cat.speak());
        assertInstanceOf(StudentWork.Animal.class, cat);
    }

    @Test
    void testCow() {
        StudentWork.Cow cow = new StudentWork.Cow();
        assertEquals("Moo!", cow.speak());
        assertInstanceOf(StudentWork.Animal.class, cow);
    }
}
