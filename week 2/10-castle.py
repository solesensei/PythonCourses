a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= d or a <= e:
    if a <= d and (b <= e or c <= e):
        print('YES')
    elif a <= e and (b <= d or c <= d):
        print('YES')
    else:
        print('NO')
elif b <= d or b <= e:
    if b <= d and c <= e:
        print('YES')
    elif b <= e and c <= d:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
