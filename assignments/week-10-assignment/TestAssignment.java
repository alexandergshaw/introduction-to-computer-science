// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testSafeDivide() {
        assertEquals(3.0, StudentWork.safeDivide(6, 2));    // normal division
        assertNull(StudentWork.safeDivide(1, 0));            // divide-by-zero handled
    }

    @Test
    void testToInt() {
        assertEquals(42, StudentWork.toInt("42", 0));        // a valid number
        assertEquals(0, StudentWork.toInt("abc", 0));        // not a number -> default 0
        assertEquals(-1, StudentWork.toInt("abc", -1));      // custom default
    }

    @Test
    void testSafeGet() {
        assertEquals(20, StudentWork.safeGet(new int[]{10, 20, 30}, 1));  // valid index
        assertNull(StudentWork.safeGet(new int[]{10, 20, 30}, 9));        // out of range -> null
    }
}
