mlist = list(map(int, input().split()))

for i in range(len(mlist)):
    if i % 2 == 0:
        print(mlist[i], end=' ')
