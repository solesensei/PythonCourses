# Pattern find in string with @

s = str(input())
pattern = str(input())

pat = pattern.split('@')

found = False
if len(pat)-1 <= len(s):
    while s and not found:
        offset = 0
        found = True
        for i, part in enumerate(pat):
            if i == 0:
                idx = a = s.find(part)
            else:
                a = 1 if s[offset:offset + len(part)] == part else -1
            if a != -1 and len(part) != 0:
                offset += len(part) + a + 1
            else:
                found = False
                break
        s = s[1 if idx <= 0 else idx:]



if found:
    print(idx)
else:
    print(-1)