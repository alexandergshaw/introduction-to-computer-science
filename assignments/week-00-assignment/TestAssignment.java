// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testHello() {
        assertEquals("Hello, world!", StudentWork.hello());
    }

    @Test
    void testFavoriteLanguage() {
        assertEquals("Java", StudentWork.favoriteLanguage());
    }

    @Test
    void testDoubleText() {
        assertEquals("abab", StudentWork.doubleText("ab"));
        assertEquals("hihi", StudentWork.doubleText("hi"));
    }
}
