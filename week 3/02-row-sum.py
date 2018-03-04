#  1+(1 / 2²)+(1 / 3²)+...+(1 / n²).
n = int(input())
s = 1.0
i = 2
while i <= n:
    s += 1 / i ** 2
    i += 1
print('{:g}'.format(s))
