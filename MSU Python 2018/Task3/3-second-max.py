# 3,4,5,6,7 - second max
s = eval(input())
a = 0
b = 0
if s:
    a = b = s[0]

for i in s:
    if i > a:
        a = i
    if i < b:
        b = i

for i in s:
    if i > b and i != a:
        b = i

if a == b:
    print('NO')
else:
    print(b)
