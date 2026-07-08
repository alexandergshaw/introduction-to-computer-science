// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testUniqueSorted() {
        assertArrayEquals(new int[]{1, 2, 3}, StudentWork.uniqueSorted(new int[]{3, 1, 3, 2}));
        assertArrayEquals(new int[]{}, StudentWork.uniqueSorted(new int[]{}));
    }

    @Test
    void testTotal() {
        assertEquals(6, StudentWork.total(new int[]{1, 2, 3}));
        assertEquals(0, StudentWork.total(new int[]{}));
    }

    @Test
    void testLargest() {
        assertEquals(9, StudentWork.largest(new int[]{3, 9, 2}));
    }
}
