# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime(x):
    if x % 2 == 0:
        if x > 2:
            return 0
        return 1
    a = int(x ** (1 / 2))
    b = 1
    while a > b:
        b = b + 1
        if x % b == 0:
            return 0
    return 1


def calculate(x):
    a = -1
    for amogus in range(1, x):
        if prime(amogus) == 1:
            a = a + amogus
    return a


print(calculate(2000000))