import sys
S = set()
c = 0
for line in sys.stdin:
    words = list(map(lambda s: s.strip(), line.split()))
    for w in words:
        if w not in S:
            c += 1
            S.add(w)
print(c)
