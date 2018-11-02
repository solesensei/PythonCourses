import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

# a b | e
# c d | f

if a == 0:
    (a, b, e, c, d, f) = (c, d, f, a, b, e)

k = c / a
(c, d, f) = (c - k*a, d - k*b, f - k*e)

y = f / d
x = (e - y*b) / a

print('{:g} {:g}'.format(x, y))
