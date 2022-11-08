# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719
# are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
# ranging a list to a set
# 8184201
f = set()
for p in range(0, 101):
    f.add(p)


#
def rota(x):
    amogus = []
    sugoma = []
    while x > 0:
        amogus.append(x % 10)
        x //= 10
    amogus.reverse()
    while len(amogus) != len(sugoma):
        a = 0
        b = 0
        for i in amogus:
            b = int(str(b) + str(i))
        sugoma.append(b)
        amogus.append(amogus[0])
        amogus.pop(0)
    print("amogus: ", amogus, "sugoma: ", sugoma)
    return sugoma


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


def rotchk(x):
    for i in rota(x):
        if not prime(i):
            return False
    return True


def calc():
    kidamogus = set()
    for i in range(2, 1000001):
        if prime(i):
            if rotchk(i):
                kidamogus.add(i)
            continue
        continue
    return kidamogus


def add(x):
    a = 0
    for i in x:
        a += i
    return a


o = calc()
print(sorted(o))
print(len(o))
