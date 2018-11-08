# Most Popular word in several strings

d = dict()

words = input().split()
while words:
    for word in words:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    words = input().split()

count = 0
max_v = 0
max_k = 'w'
for k, v in sorted(d.items(), key=lambda x: -x[1]):
    if count:
        if v == max_v:
            max_k = '---'
        break
    max_k = k
    max_v = v
    count += 1

print(max_k)
