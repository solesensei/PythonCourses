n = int(input())
d = {}
for i in range(n):
    line = list(map(lambda s: s.strip(), input().split()))
    d[line[0]] = line[1]
    d[line[1]] = line[0]
word = input()
print(d.get(word, 0))
