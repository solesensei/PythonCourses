mlist = list(map(int, input().split()))

nlist = []
i = 1
while i < len(mlist):
    nlist.append(mlist[i])
    i += 2
i = 0
j = 1
while i < len(mlist):
    nlist.insert(j, mlist[i])
    i += 2
    j += 2
for x in nlist:
    print(x, end=' ')
