// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testGreet() {
        assertEquals("Hello, Sam!", StudentWork.greet("Sam"));
        assertEquals("Hello, Ada!", StudentWork.greet("Ada"));
    }

    @Test
    void testLoud() {
        assertEquals("HI", StudentWork.loud("hi"));
        assertEquals("WOW", StudentWork.loud("Wow"));
    }

    @Test
    void testAddExcitement() {
        assertEquals("go!", StudentWork.addExcitement("go"));
    }
}
