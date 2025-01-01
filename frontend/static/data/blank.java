import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {

    public static List<Integer> getPrimeNumbers(int start, int end) {
        List<Integer> primeNumbers = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                primeNumbers.add(i);
            }
        }
        return primeNumbers;
    }

    private static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<Integer> primes = getPrimeNumbers(1, 100);
        System.out.println("Prime numbers from 1 to 100: " + primes);
    }
}

// Unit test for PrimeNumbers class
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PrimeNumbersTest {

    @Test
    public void testGetPrimeNumbers() {
        List<Integer> expectedPrimes = List.of(
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        );
        
        List<Integer> actualPrimes = PrimeNumbers.getPrimeNumbers(1, 100);
        assertEquals(expectedPrimes, actualPrimes);
    }

    @Test
    public void testIsPrime() {
        assertTrue(PrimeNumbers.isPrime(2));
        assertTrue(PrimeNumbers.isPrime(3));
        assertFalse(PrimeNumbers.isPrime(4));
        assertTrue(PrimeNumbers.isPrime(5));
        assertFalse(PrimeNumbers.isPrime(1));
        assertFalse(PrimeNumbers.isPrime(0));
        assertFalse(PrimeNumbers.isPrime(-1));
    }
}

