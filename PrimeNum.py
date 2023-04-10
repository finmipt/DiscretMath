import unittest


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24]
        for n in primes:
            self.assertTrue(is_prime(n))
        for n in non_primes:
            self.assertFalse(is_prime(n))


if __name__ == '__main__':
    unittest.main()
