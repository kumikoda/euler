# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
# Find the sum of a Pythagorean triplet where
#     a + b + c = 1000

def find_trip(n):
    for a in range(1,n-2):
        for b in range(1,n-2-a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
    return -1

print find_trip(1000)
