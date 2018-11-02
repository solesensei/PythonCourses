import sys

d = {}
for line in sys.stdin:
    words = line.split()
    for w in words:
        d[w] = d.get(w, 0) + 1
mw = list()
m = 0
for w, n in d.items():
    if n >= m:
        if n > m:
            mw.clear()
            m = n
        mw.append(w)
mw.sort()
print(mw[0])
