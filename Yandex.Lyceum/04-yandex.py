def next_min(dif, flg):
    i = 1
    mmin = 0
    k = 0
    while i < len(dif)-1:
        if flg[i] == 0 and (dif[i] < mmin or mmin == 0):
                mmin = dif[i]
                k = i
        i += 1
    flg[k] = 1
    return mmin


def check_rope(flg):
    isFinished = True
    for i in range(len(flg) - 1):
        if flg[i] == 0 and flg[i+1] == 0:
            isFinished = False
    print(isFinished)
    return isFinished

N = int(input())
line = input()
vec = line.split(' ')
while vec.count('') > 0:
    vec.remove('')
for i, item in enumerate(vec):
    vec[i] = int(item)
vec.sort()
dif = [N for i in range(N-1)]
flg = [0 for i in range(N-1)]
for i in range(N-1):
    dif[i] = vec[i+1] - vec[i]
print(vec)
print(dif)
i = 1
s = dif[0] + dif[N-2]
flg[0], flg[N-2] = 1, 1
while i < N-3:
    if check_rope(flg):
        break
    s += next_min(dif, flg)
    print(s)
    print(flg)
    i += 1
print(s)
