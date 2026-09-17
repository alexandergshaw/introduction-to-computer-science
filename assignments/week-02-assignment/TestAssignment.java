// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testRectangleArea() {
        assertEquals(12.0, StudentWork.rectangleArea(3, 4));
        assertEquals(25.0, StudentWork.rectangleArea(5, 5));
    }

    @Test
    void testSquare() {
        assertEquals(16.0, StudentWork.square(4));
        assertEquals(100.0, StudentWork.square(10));
    }

    @Test
    void testAverage() {
        assertEquals(5.0, StudentWork.average(4, 6));
        assertEquals(5.0, StudentWork.average(10, 0));
    }
}
