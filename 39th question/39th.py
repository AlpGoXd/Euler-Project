# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
def pisagor(a):
    amogus = []
    x = int(a**(1/2))
    y = (a * (a - 2 * x)) / (2 * (a - x))
    z = ((x ** 2) + (y ** 2)) ** (1 / 2)
    while x > y or x > z:
        y = (a * (a - 2 * x)) / (2 * (a - x))
        z = ((x ** 2) + (y ** 2)) ** (1 / 2)
        if float(y) == int(y) and float(z) == int(z):
            amogus.append([x, y, z])
            print(x, y, z)
        x = x - 1
    return amogus


print(pisagor(120))
