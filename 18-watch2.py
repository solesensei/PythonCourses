n = int(input())
h = n//60//60 % 24
m = n//60 % 60
s = n % 60
print(h, ':', m // 10, m % 10 , ':', s // 10, s % 10, sep='')
