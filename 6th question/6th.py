def sugoma(x):
    a = 0
    b = 0
    for i in range(1, x + 1):
        a = i ** 2 + a
        b += i
    b = b ** 2
    return b - a


print(sugoma(100))
