# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt

def is_prime(x):
    N = int(sqrt(x))
    odds = range(1, N+1, 2)
    for i in odds[1:]:
        if x % i == 0:
            return False

    return True

def largest_prime_factor(x):
    N = int(sqrt(x))
    odds = range(1, N+1, 2)
    for i in reversed(odds):
        if x % i == 0 and is_prime(i):
            return i

    return 1

print largest_prime_factor(600851475143)
