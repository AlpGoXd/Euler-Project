# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pisagor(a):
    x = 1
    y = (a * (a - 2 * x)) / (2 * (a - x))
    z = ((x ** 2) + (y ** 2)) ** (1 / 2)
    while not (int(y) == float(y) and int(z) == float(z)):
        x = x + 1
        y = (a * (a - 2 * x)) / (2 * (a - x))
        z = ((x ** 2) + (y ** 2)) ** (1 / 2)
    print(x, y, z)
    return x * y * z


print(pisagor(1000))
