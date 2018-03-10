s = input()
s1, s2, s3 = s.split(' ')
a = float(s1)
b = float(s2)
c = float(s3)
a, b, c = sorted([a, b, c])
res = -1
if a + b > c:
    if a**2 + b**2 == c**2:
        res = 0
    elif (a**2 + b**2 - c**2) / (2*a*b) < 0:
        res = 2
    else:
        res = 1
print(res)
