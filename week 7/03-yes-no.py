L = list(map(int, input().split()))
S = set()
for e in L:
    if e in S:
        print('YES')
    else:
        print('NO')
        S.add(e)
