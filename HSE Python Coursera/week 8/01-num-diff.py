from itertools import combinations


s = map(int, input().split())
s = sorted(s)

print(*zip(filter(lambda x: int(x[0] == x[1]), combinations(s, 2))))
