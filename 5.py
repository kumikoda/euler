# Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from math import sqrt

# first attempt, this thing works for 10 but is too slow for 20
def smallest_multiple(x):
    y = 1
    while(True):
        print ydd
        divisible = True
        for i in range(1, x+1):
            if y % i != 0:
                divisible = False

        if divisible is True:
            return y

        y = y + 1

# the problem with above is that we are checking way too many numbers
# we are checking from 1-20!, which is a large ass number

# what if we checked from just the product of all primes to 20! ?
# that is still too much, but the answer has to be a multiple of the product of all primes...
# so instead of incrementing one by one, we can increment by that product!
def is_prime(x):
    N = int(sqrt(x))+1
    for i in range(2, N):
        if x % i == 0:
            return False
    return True

def primes_under(x):
    primes = []
    for i in range(1, x+1):
        if is_prime(i):
            primes.append(i)
    return primes

def factorial(x):
    product = 1
    for i in range(1, x+1):
        product = product * i
    return product

# is x evenly divisible by [1,a]?
def is_evenly(x, a):
    for i in range(1, a+1):
        if x % i != 0:
            return False
    return True

def smallest_multiple2(x):
    n = reduce((lambda x, y: x * y), primes_under(x))
    N = factorial(x)
    for i in range(n, N, n):
        print i
        if is_evenly(i, x) is True:
            return i

# okay this is still too slow since we need to check N/n = 250822656000 numbers,
# can we do something smarter?

# okay so we need to prune the list of numbers a bit before mulitpling them all together
# doing just the primes wont work because just because x is divisible by 3 does not mean it is by 9
# but the reverse is true! if x is div by 9 then we can skip 3
# what if we worked our way up and removed all the lower numbers?

# 10 --> 10, 9, 8, 7, 6, 5x, 4x, 3x, 2x, 1x
def prune(x):
    pruned = []
    for i in range(1, x+1):
        for j in pruned:
            if i % j == 0:
                pruned.remove(j)
                break
        pruned.append(i)

    return pruned

def fold(xs):
    product = 1
    for x in xs:
        product = product * x
    return product

# using prune and fold instead of factorial to set the upper bound
def smallest_multiple3(x):
    n = reduce((lambda x, y: x * y), primes_under(x))
    N = fold(prune(x))
    for i in range(n, N, n):
        if is_evenly(i, x) is True:
            return i

print smallest_multiple3(20)

