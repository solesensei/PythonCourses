a = int(input())
b = int(input())
c = int(input())

eq = (a == b) + (a == c) + (b == c)

if eq == 1:
    eq += 1
print(eq)
