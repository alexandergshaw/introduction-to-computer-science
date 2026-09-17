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
    void testTotal() {
        assertEquals(6, StudentWork.total(new int[]{1, 2, 3}));
    }

    @Test
    void testGreet() {
        assertEquals("Hello, Sam!", StudentWork.greet("Sam"));
    }
}
