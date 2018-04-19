inFile = open('input.txt', 'r', encoding='utf-8')
count = {}
for line in inFile:
    words = map(lambda s: s.strip(), line.split())
    for word in words:
        print(count.get(word, 0), end=' ')
        count[word] = count.get(word, 0) + 1
print()
