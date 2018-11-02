import math

a = float(input())
b = float(input())
c = float(input())

if c == 0:
    if b == 0:
        print(0)
    else:
        x1 = 0
        x2 = -b / a
        if x2 < x1:
            (x1, x2) = (x2, x1)
        print('{:g} {:g}'.format(x1, x2))
elif b == 0:
    k = -c / a
    if k > 0:
        x1 = -math.sqrt(k)
        x2 = math.sqrt(k)
        if x2 < x1:
            (x1, x2) = (x2, x1)
        print('{:g} {:g}'.format(x1, x2))
else:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        if x2 < x1:
            (x1, x2) = (x2, x1)
        print('{:g} {:g}'.format(x1, x2))
    elif d == 0:
        x = -b / (2*a)
        print('{:g}'.format(x))
