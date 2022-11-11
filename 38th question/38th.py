# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

def count(x):
    a = 1
    while x // 10 > 0:
        x //= 10
        a += 1
    return a


def pan(x):
    zer = {0}
    h = set()
    a = count(x)
    while a - 1 >= 0:
        a -= 1
        h.add(x % 10)
        x //= 10
    if len(h) == 9 and len(h.intersection(zer)) == 0:
        return True
    else:
        return False


def creat(x):
    a = ""
    for i in range(1, 10):
        a = a + str(x * i)
        if len(a) == 9:
            return int(a)
        elif len(a) > 9:
            return 0
    return 0


def calc():
    a = 0
    b = 0
    c = ""
    for i in range(3):
        for k in range(0, i + 1):
            c = c + "1"
        for j in range(10 ** i, int(c) * 9 + 1):
            print(j)
            if pan(creat(j)) and creat(j) > a:
                b = j
                a = creat(j)
    print(a, b)


calc()
