n = int(input())
last = n % 10
last2 = n % 100

print(n, end=' ')
if last == 0 or 5 <= last <= 9 or 11 <= last2 <= 14:
    print('korov')
elif last == 1:
    print('korova')
else:
    print('korovy')
