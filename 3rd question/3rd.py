# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
number = 600851475143
# FIXED :D
def den(x):
    a = 0
    set = []
    while x % 2 == 0:
        x = x/2
        set.append(2)
    while x >= a + 1:
        a = a + 1
        if x % a == 0:
            set.append(a)
            x = x/a
    return set


def prime(x):
    mek = list()
    for y in x:
        a = 1
        b = int
        while y > a + 1:
            a = a + 1
            if y / a == y // a:
                b = 1
        if b != 1:
            mek.append(y)
    return mek

print(prime(den(number)))
