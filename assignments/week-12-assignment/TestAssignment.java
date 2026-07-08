// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testClamp() {
        assertEquals(5.0, StudentWork.clamp(5, 0, 10));    // already inside the range
        assertEquals(0.0, StudentWork.clamp(-3, 0, 10));   // too low  -> snaps up to 0
        assertEquals(10.0, StudentWork.clamp(99, 0, 10));  // too high -> snaps down to 10
    }

    @Test
    void testInRange() {
        assertTrue(StudentWork.inRange(5, 0, 10));
        assertFalse(StudentWork.inRange(15, 0, 10));
    }

    @Test
    void testSign() {
        assertEquals(1, StudentWork.sign(7));
        assertEquals(-1, StudentWork.sign(-7));
        assertEquals(0, StudentWork.sign(0));
    }
}
