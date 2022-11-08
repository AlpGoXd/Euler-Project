# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def fact(x):
    a = 1
    b = 1
    while x >= a:
        b *= a
        a += 1
    return b


def srt(x):
    amogus = []
    while x > 0:
        amogus.append(x % 10)
        x = x // 10
    return amogus


def chk(x):
    a = 0
    for i in srt(x):
        a += fact(i)
    if x == a:
        return True
    else:
        return False


def test():
    c = 362880
    a = 362880
    b = 9
    while a > b:
        a += c
        b = int(str(b) + "9")
    print(a, b)


def calc():
    sugoma = []
    for i in range(3, 9999999 + 1):
        if chk(i):
            sugoma.append(i)
        continue
    return sugoma


def add(x):
    a = 0
    for i in x:
        a += i
    return a


print(add(calc()))
