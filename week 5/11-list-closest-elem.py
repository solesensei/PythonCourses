n = int(input())
mlist = list(map(int, input().split()))
x = int(input())
result = 0
if max(mlist) < x:
    result = max(mlist)
elif min(mlist) > x:
    result = min(mlist)
else:
    close = abs(mlist[0] - x)
    for i in mlist:
        if abs(i - x) < close:
            close = abs(i - x)
            result = i
print(result)
