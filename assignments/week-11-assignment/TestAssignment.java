// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testIsPalindrome() {
        assertTrue(StudentWork.isPalindrome("racecar"));
        assertFalse(StudentWork.isPalindrome("hello"));
    }

    @Test
    void testIsEven() {
        assertTrue(StudentWork.isEven(4));
        assertFalse(StudentWork.isEven(7));
    }

    @Test
    void testAbsolute() {
        assertEquals(5.0, StudentWork.absolute(-5));
        assertEquals(3.0, StudentWork.absolute(3));
        assertEquals(0.0, StudentWork.absolute(0));
    }
}
