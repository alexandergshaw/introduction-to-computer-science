// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testClassify() {
        assertEquals("positive", StudentWork.classify(5));
        assertEquals("negative", StudentWork.classify(-2));
        assertEquals("zero", StudentWork.classify(0));
    }

    @Test
    void testIsEven() {
        assertTrue(StudentWork.isEven(4));
        assertFalse(StudentWork.isEven(7));
    }

    @Test
    void testLarger() {
        assertEquals(9.0, StudentWork.larger(3, 9));
        assertEquals(8.0, StudentWork.larger(8, 2));
    }
}
