# fraction reduce   
s = eval(input())
m = s[0]
n = s[1]
z = m // n
m -= n * z
for i in range(m, 1, -1):
    if m % i == 0 == n % i:
        m //= i
        n //= i
        i = m
if z:
    print(z, end='')
if m > 0:
    print(' ', m, '/', n, sep='')