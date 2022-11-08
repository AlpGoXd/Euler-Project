# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
def binar(x):
    return int(str(bin(x))[2:])


def inv(x):
    a = 0
    while x > 0:
        c = x % 10
        a = a * 10 + c
        x = x // 10
    return a


def pali(x):
    if x == inv(x):
        return 1
    else:
        return 0


def palichk():
    amogus = []
    for i in range(1000001):
        if pali(i) and pali(binar(i)):
            amogus.append(i)
    return amogus


def add(x):
    a = 0
    for i in x:
        a += i
    return a


p = palichk()
print(p)
print(add(p))
for i in p:
    print(binar(i), end="||")
