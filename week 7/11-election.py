inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
d = {}
votes = 0
for name in inFile:
    name = name[:-1] if name[-1] == '\n' else name
    d[name] = d.get(name, 0) + 1
    votes += 1
num = 2
for name, vote in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(name, file=outFile)
    num -= 1
    if vote / votes > 0.5:
        break
    if num == 0:
        break
