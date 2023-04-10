def eratosthenes(n):
    numbers = list(range(2, n + 1))
    is_prime = [True] * len(numbers)

    for i in range(len(numbers)):
        if is_prime[i]:
            for j in range(i + 1, len(numbers)):
                if numbers[j] % numbers[i] == 0:
                    is_prime[j] = False

    primes = []
    for i in range(len(numbers)):
        if is_prime[i]:
            primes.append(numbers[i])

    return primes


def factorize(n):
    dividers = []
    primes = eratosthenes(n)
    for prime in primes:
        while n % prime == 0:
            dividers.append(prime)
            n = n / prime
            if n < prime:
                return dividers
    return dividers


print(factorize(490))
