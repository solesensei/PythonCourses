h = int(input())
a = int(input())
b = int(input())

print((h - h % (a-b) - a + 1) // (a-b))
