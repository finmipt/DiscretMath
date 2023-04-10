from math import gcd
from typing import List, Tuple


def extended_euclidean_algorithm(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return 1, 0, a
    else:
        x1, y1, gcd_ab = extended_euclidean_algorithm(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y, gcd_ab


def linear_congruence(a: int, b: int, m: int) -> Tuple[bool, List[int]]:
    solutions = []
    d = gcd(a, m)
    if b % d == 0:
        a1 = a // d
        b1 = b // d
        m1 = m // d
        x0, y0, _ = extended_euclidean_algorithm(a1, m1)
        x = x0 * b1 % m1
        for i in range(d):
            solutions.append(x + i * m1)
        return True, solutions
    else:
        return False, solutions


print(linear_congruence(10, 15, 11))
