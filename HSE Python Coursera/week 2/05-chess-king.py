x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

str_dif = abs(x1 - x2)
col_dif = abs(y1 - y2)

if str_dif <= 1 and col_dif <= 1:
    print("YES")
else:
    print("NO")
