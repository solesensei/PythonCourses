a = int(input())
b = int(input())
c = int(input())

if b <= a and b <= c:
    (a, b, c) = (b, a, c)
elif c <= a and c <= b:
    (a, b, c) = (c, a, b)
if b >= c:
    (a, b, c) = (a, c, b)

print(a, b, c)
