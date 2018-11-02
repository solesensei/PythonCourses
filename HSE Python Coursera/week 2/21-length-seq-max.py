n = int(input())

m = n
length = 1
i = 1
while n != 0:
    n = int(input())
    if n == m:
        i += 1
        if length < i:
            length = i
    else:
        i = 1
        m = n

print(length)
