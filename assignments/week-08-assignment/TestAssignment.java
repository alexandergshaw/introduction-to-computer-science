// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testRectangle() {
        assertEquals(6.0, new StudentWork.Rectangle(2, 3).area());
        assertEquals(20.0, new StudentWork.Rectangle(4, 5).area());
    }

    @Test
    void testSquare() {
        assertEquals(16.0, new StudentWork.Square(4).area());
    }

    @Test
    void testPerson() {
        assertEquals("Hi, I'm Ada", new StudentWork.Person("Ada").greet());
    }
}
