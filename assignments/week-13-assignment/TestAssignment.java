// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testFormatFullName() {
        assertEquals("Ada Lovelace", StudentWork.formatFullName("Ada", "Lovelace"));
        assertEquals("Ada Lovelace", StudentWork.formatFullName("  Ada ", "Lovelace "));
    }

    @Test
    void testInitials() {
        assertEquals("A.L.", StudentWork.initials("Ada", "Lovelace"));
        assertEquals("G.H.", StudentWork.initials("grace", "hopper"));
    }

    @Test
    void testSlugify() {
        assertEquals("hello-world", StudentWork.slugify("  Hello World "));
    }
}
