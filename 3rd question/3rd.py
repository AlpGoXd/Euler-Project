# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
number = 600851475143
#TAKES TOO LONG

def den(x):
    a = 0
    set = []
    while x > a + 1:
        a = a + 1
        print(a)
        if x / a == x // a:
            set.append(a)
    return set


def prime(x):
    for y in x:
        a = 1
        b = int
        while y > a + 1:
            a = a + 1
            if y / a == y // a:
                b = 1
        if b != 1:
            print(y)


print(prime(den(number)))
