n = int(input())
m1 = n
m2 = -1
while n != 0:
    n = int(input())
    if n >= m1:
        m2, m1 = m1, n
    elif m2 < n < m1:
        m2 = n
print(m2)
