import sys


def sortingValue(items):
    return items[1]


def sortingKey(items):
    return items[0]

d = {}
for line in sys.stdin:
    words = list(map(lambda s: s.strip(), line.split()))
    for w in words:
        d[w] = d.get(w, 0) + 1

s = []
tmp = []
val = 0
for w, v in sorted(d.items(), key=sortingValue, reverse=True):
    if val != v:
        for e in sorted(tmp, key=sortingKey):
            s.append(e)
        val = v
        tmp.clear()
    tmp.append((w, v))
for e in sorted(tmp, key=sortingKey):
    s.append(e)

for i in range(len(s)):
    print(s[i][0])
