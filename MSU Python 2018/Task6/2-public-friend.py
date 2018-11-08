# Public Friend Pairs found

familiar = dict()
pair = eval(input())
while pair != (0, 0):
    for i in range(2):
        familiar.setdefault(pair[i], set({pair[i]})).add(pair[1 - i])
    pair = eval(input())

people_count = len(familiar)
for k, v in familiar.items():
    if len(v) == people_count:
        print(k, end=' ')
print()
