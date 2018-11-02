# Pattern find in string with @

s = str(input())
pattern = str(input())

pat = pattern.split('@')

found = False
while s and not found:
    offset = 0
    found = True
    for i, part in enumerate(pat):
        if i == 0:
            idx = a = s.find(part)
        else:
            s.find(part, offset, offset + len(part))
        if a != -1:
            offset = len(part) + idx + 1
        else:
            found = False
            break
    s = s[1:]


if found:
    print(idx)
else:
    print(-1)