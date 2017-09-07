# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Strategy: instead of checking if a number if prime, only check if it is relatively prime!
def is_relative_prime(a, bs):
    for b in bs:
        if a % b == 0:
            return False
    return True


def nth_prime(n):
    primes = [2]
    curr = 3
    while len(primes) < n:
        if is_relative_prime(curr, primes):
            primes.append(curr)
        curr = curr + 2

    return primes[-1]

# HELL YEAH FIRST TRY!
print nth_prime(10001)
