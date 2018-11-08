# Most popular words in string

words = input().upper().split()
d = dict()

for word in words:
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

k = sorted(d.values(), reverse=True)[0]
count = 0
for i in sorted(d.values(), reverse=True):
    if i != k:
        break
    count += 1

print(count)
