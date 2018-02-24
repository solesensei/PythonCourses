x = int(input())
big = x
while x != 0:
    if x > big:
        big = x
    x = int(input())
print(big)
