# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# without programming, just doing some math.....
# (a + b)^2 = a^2 + b^2 + 2ab
# sum_square_diff(a, b) = 2ab

# (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc
# sum_square_diff(a, b) = 2ab + 2ac + 2bc

# therefore sum square diff ==> sum(product of every pair)

def sum_square_diff(xs):
    c = 0
    for x in xs:
        for y in xs:
            if x != y:
                c = c + x*y
    return c

def sum(xs):
    return reduce(lambda x,y: x+y, xs)

def square(xs):
    return map(lambda x: x**2, xs)

# here is the "easy" way, wrote it just to check my answer
def sum_square_diff2(xs):
    square_sum = sum(xs)**2
    sum_square = sum(square(xs))

    return square_sum - sum_square


print sum_square_diff2(range(1,101))
print sum_square_diff(range(1,101))
