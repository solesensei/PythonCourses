s = input()

first = pos = s.find('h')
while pos != -1:
    last = pos
    pos = s.find('h', pos+1)

print(s[:first] + s[last+1:])
