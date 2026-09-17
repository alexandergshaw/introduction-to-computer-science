// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testLetterGrade() {
        assertEquals("A", StudentWork.letterGrade(95));
        assertEquals("B", StudentWork.letterGrade(85));
        assertEquals("C", StudentWork.letterGrade(72));
        assertEquals("D", StudentWork.letterGrade(65));
        assertEquals("F", StudentWork.letterGrade(40));
    }

    @Test
    void testAverage() {
        assertEquals(4.0, StudentWork.average(new double[]{2, 4, 6}));
    }

    @Test
    void testCountPositives() {
        assertEquals(2, StudentWork.countPositives(new double[]{-1, 2, 0, 5}));
        assertEquals(0, StudentWork.countPositives(new double[]{-3, -2}));
    }
}
