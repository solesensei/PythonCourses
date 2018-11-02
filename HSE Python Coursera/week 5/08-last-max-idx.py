mlist = list(map(int, input().split()))
m = mlist[0]
idx = 0
for i, v in enumerate(mlist):
    if v >= m:
        m, idx = v, i
print(m, idx)
