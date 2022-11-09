# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly, we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.


def prime(x):
    if x % 2 == 0:
        if x == 2:
            return True
        else:
            return False
    if x == 1:
        return False
    a = int(x ** (1 / 2))
    for i in range(2, a + 1):
        if x % i == 0:
            return False
    return True


def cut(x):
    a = str(x)
    b = str(x)
    amogus = set()
    for i in range(len(b) - 1, 0, -1):
        amogus.add(int(b[:-i]))
    for j in range(0, len(a)):
        amogus.add(int(a[j:]))
    return amogus


def find():
    star = 0
    a = 7
    amogus = []
    while 11 > star:
        a += 1
        b = True
        for i in cut(a):
            if not prime(i):
                b = False
                break
        if b:
            print(a)
            amogus.append(a)
            star += 1
    return amogus


def add(x):
    a = 0
    for i in x:
        a += i
    return a


print(add(find()))
