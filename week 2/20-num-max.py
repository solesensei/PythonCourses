n = int(input())

m = n
num = 0
while n != 0:
    if n > m:
        m = n
        num = 0
    if n == m:
        num += 1
    n = int(input())
print(num)
