n = int(input())
s = {i for i in range(1, n+1)}
line = input()
while line != 'HELP':
    q = set(map(int, line.split()))
    line = input().strip()
    if line == 'YES':
        s &= q
    elif line == 'NO':
        s -= q
    line = input().strip()

for i in range(n+1):
    if i in s:
        print(i, end=' ')
print()
