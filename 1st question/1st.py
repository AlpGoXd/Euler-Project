# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
while 1000 > b*3:
    a = a+b*3
    b = b+1
print("------------")
while 1000 > d*5:
    c = c+d*5
    d = d+1
while 1000 > f*15:
    e = e+f*15
    f = f+1
print(e)
print(a+c-e)