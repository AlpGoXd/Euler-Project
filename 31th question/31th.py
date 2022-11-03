# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
# circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p). How many ways can £2 be made using any
# number of coins?

def fact(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a


def comb(x, y):
    if y > x:
        print("combination error")
        return 0
    a = fact(x) / (fact(y) * fact(x - y))
    return int(a)


pra = [1, 2, 5, 10, 20, 50, 100, 200]
t = 200
