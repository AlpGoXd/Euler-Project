# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def ebob(x, y):
    b = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            b = i
    return b


def ekok(x):
    a = 1
    for i in x:
        a = int((a * i) / ebob(a, i))
    return a


print(ekok(range(1, 21)))
