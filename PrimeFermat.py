import unittest


def perfect_square(x):
    return (int(x ** 0.5)) ** 2 == x


def is_prime_fermat(n):
    x = int(n ** 0.5) + 1
    if n==2:
        return True
    if n%2 == 0 or perfect_square(n):
        return False
    while not perfect_square(x * x - n):
        x += 1
    y = int((x * x - n) ** 0.5)
    a = x - y
    b = x + y
    if a == 1 or b ==1:
        return True
    else:
        return False


class TestIsPrimeFermat(unittest.TestCase):

    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 2017]
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 35, 36, 49, 90, 125, 1008]
        for n in primes:
            self.assertTrue(is_prime_fermat(n))
        for n in non_primes:
            self.assertFalse(is_prime_fermat(n))


print(is_prime_fermat(25))
if __name__ == '__main__':
    unittest.main()