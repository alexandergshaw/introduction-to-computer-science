// ─────────────────────────────────────────────────────────────────────────────
// Automated tests. You don't edit this file — but READING it shows you exactly
// what each class and method should do. Run it from your IDE; aim for all green.
// ─────────────────────────────────────────────────────────────────────────────
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestAssignment {

    @Test
    void testBankAccount() {
        StudentWork.BankAccount acct = new StudentWork.BankAccount();  // starts at 0
        assertEquals(0.0, acct.balance);
        acct.deposit(100);     // +100
        acct.withdraw(30);     // -30
        assertEquals(70.0, acct.balance);
        assertEquals(50.0, new StudentWork.BankAccount(50).balance);   // opening balance
    }

    @Test
    void testSafeDivide() {
        assertEquals(3.0, StudentWork.safeDivide(6, 2));
        assertNull(StudentWork.safeDivide(1, 0));
    }

    @Test
    void testIsPalindrome() {
        assertTrue(StudentWork.isPalindrome("racecar"));
        assertFalse(StudentWork.isPalindrome("hello"));
    }
}
