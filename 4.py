# Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.
from math import sqrt

# reverse list using slice
def rev(a):
    return a[::-1]

# cheap string method, might be slow
def is_palindrome(x):
    chars = list(str(x))
    n = len(chars)/2
    if len(chars) % 2 == 0:
        left = chars[:n]
        right = chars[n:]
        return left == rev(right)
    else:
        left = chars[:n]
        right = chars[n+1:]
        return left == rev(right)

def largest_palindrome_product(digits):
    mx = pow(10, digits)
    mn = pow(10, digits-1)
    ps = []
    for x in range(mn, mx):
        for y in range(mn, mx):
            if is_palindrome(x*y):
                ps.append(x*y)

    return max(ps)

print largest_palindrome_product(3)
