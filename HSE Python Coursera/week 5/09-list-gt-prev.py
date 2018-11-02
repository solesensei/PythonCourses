mlist = list(map(int, input().split()))

for i in range(1, len(mlist)):
    if mlist[i] > mlist[i-1]:
        print(mlist[i], end=' ')
