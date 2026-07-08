// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testAdd() {
        assertEquals(5.0, StudentWork.add(2, 3));       // two-arg version
        assertEquals(9.0, StudentWork.add(2, 3, 4));    // three-arg version
    }

    @Test
    void testGreet() {
        assertEquals("Hello, Sam!", StudentWork.greet("Sam"));          // default greeting
        assertEquals("Hi, Sam!", StudentWork.greet("Sam", "Hi"));       // custom greeting
    }

    @Test
    void testTriple() {
        assertEquals(15.0, StudentWork.triple(5));
    }
}
