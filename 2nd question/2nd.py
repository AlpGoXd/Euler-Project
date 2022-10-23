# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
def even(x):
    if x / 2 == x // 2:
        return 1
    else:
        return 0


a = 1
b = 0
c = 0
d = 0
while 4000000 > c:
    c = a + b
    b = a
    a = c
    if even(c) == 1:
        d = d + c
print(d)
