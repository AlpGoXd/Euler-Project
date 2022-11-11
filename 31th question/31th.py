# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
# circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p). How many ways can £2 be made using any
# number of coins?
# HARDEST ONE SO FAR REQUIRES
# UNDERSTANDING DYNAMIC PROGRAMMING

coins = [2, 5, 10, 20, 50, 100, 200]


def sus(x, y):
    amogus = []
    for i in range(y + 1):
        amogus.append(1)
    for j in x:
        for k in range(y + 1):
            if k >= j:
                amogus[k] += amogus[k - j]
    print(amogus)
    return amogus[y]


print(sus(coins, 200))
