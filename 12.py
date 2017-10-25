from math import sqrt, floor

def divisors(n):
    ds = []
    for i in range(1, n+1):
        if n % i == 0:
            ds.append(i)
    return len(ds)

def divisors2(n):
    c = 0
    for i in range(1, int(sqrt(n+1))):
        if n % i == 0:
            c = c + 2
    return c

def triangle_div(n):
    sum = 0
    i = 0
    while True:
        if divisors2(sum) > n:
            return sum
        i = i + 1
        sum = sum + i

print divisors(28)
print divisors2(28)
print triangle_div(500)
