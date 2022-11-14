# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
def pisagor(a):
    x = 1
    amogus = []
    y = (a * (a - 2 * x)) / (2 * (a - x))
    z = ((x ** 2) + (y ** 2)) ** (1 / 2)
    while y > x and z > x:
        if int(y) == float(y) and int(z) == float(z):
            amogus.append([x, y, z])
        x = x + 1
        y = (a * (a - 2 * x)) / (2 * (a - x))
        z = ((x ** 2) + (y ** 2)) ** (1 / 2)
    return amogus


def calc(x):
    a = 0
    b = 0
    for i in range(2, x+1):
        c = pisagor(i)
        if len(c) > b:
            a = i
            b = len(c)
        continue
    return a

print(calc(1000))
