# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct,is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import math


def calc():
    amogus = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                a = int(str(i) + str(j))
                b = int(str(k) + str(i))
                if a / b == j / k and a != b:
                    amogus.append([a, b])
                continue

    return amogus


def adder(x):
    a = 1
    b = 1
    for i in range(len(x)):
        a *= x[i][1]
        b *= x[i][0]
    print(a ,b ,a/b)
    return b / math.gcd(a, b)

print(adder(calc()))