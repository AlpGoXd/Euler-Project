# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit number
def inv(x):
    a = 0
    while x > 0:
        c = x % 10
        a = a * 10 + c
        x = x // 10
    return a


def pali(x):
    if 10 > x >= 0:
        return 0
    if x == inv(x):
        return 1
    else:
        return 0


def find(z):
    found = set()
    for x in range(z):
        a = 0
        while x >= a:
            c = x * a
            if pali(c) == 1:
                found.add(c)
            a = a + 1
    return found


print(sorted(find(1000)))