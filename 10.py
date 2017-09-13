# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt

def is_prime(x, primes):
    for p in primes:
        if x % p == 0:
            return False
        if p > sqrt(x):
            break
    return True

def sum_of_primes(n):
    primes = [2]
    total = 2
    for i in range(3, n, 2):
        if is_prime(i, primes):
            primes.append(i)
            total = total + i
    return total

print sum_of_primes(2000000)
