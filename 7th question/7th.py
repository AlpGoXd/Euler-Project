# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime(x):
    if x % 2 == 0:
        if x > 2:
            return 0
        return 1
    a = int(x ** (1/2))
    b = 1
    while a > b:
        b = b + 1
        if x % b == 0:
            return 0
    return 1

def sugoma(x):
    a = 0
    b = 1
    while x != a:
        b = b + 1
        if prime(b) == 1:
            a = a + 1
    return b

print(sugoma(10001))

