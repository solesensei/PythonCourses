x = int(input())
y = int(input())

flats = y - x + 1

if x == 1 or y % flats == 0:
    print('YES')
else:
    print('NO')
