# Pattern find in string with @

s = str(input())
pattern = str(input())

pat = pattern.split('@')
found = False
idx = 0
absolute_idx = 0
if len(pat)-1 <= len(s):
    while s and not found and idx != -1:
        offset = 0
        found = True
        for i, part in enumerate(pat):
            if i == 0:
                idx = a = s.find(part)
            else:
                a = 0 if s[offset:offset + len(part)] == part else -1
            if a != -1:
                offset += len(part) + a + 1
            else:
                found = False
                break
        if found and idx == 0:
            break
        absolute_idx += 1 if idx <= 0 else idx
        s = s[1 if idx <= 0 else idx:]

if found:
    print(absolute_idx)
else:
    print(-1)
