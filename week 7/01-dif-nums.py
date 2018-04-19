l = map(int, input().split())
s = set()
c = 0
for e in l:
    if e not in s:
        c += 1
        s.add(e)
print(c)
