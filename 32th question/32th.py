# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def count(x):
    a = 1
    while x // 10 > 0:
        x //= 10
        a += 1
    return a


def counts(x, y):
    l = count(x) + count(y) + count(x * y)
    return l


def calc():
    susl = []
    for i in range(0, 10000):
        for j in range(0, 101):
            if counts(i, j) == 9:
                susl.append([i, j, i * j])

    return susl


def setter(x):
    h = set()
    a = count(x)
    while a - 1 >= 0:
        a -= 1
        h.add(x % 10)
        x //= 10
    return h


def pan(x):
    sus = list()
    zer = {0}
    for i in range(0, len(x)):
        a = set(setter(x[i][0]))
        a = a.union(set(setter(x[i][1])))
        a = a.union(set(setter(x[i][2])))
        if len(a.intersection(zer)) == 0 and len(a) == 9:
            sus.append([x[i][0], x[i][1], x[i][2]])
    return sus


def adder(x):
    amogus = set()
    a = 0
    for i in range(len(x)):
        amogus.add(x[i][2])
    for j in amogus:
        a += j
    return a


print(adder(pan(calc())))
