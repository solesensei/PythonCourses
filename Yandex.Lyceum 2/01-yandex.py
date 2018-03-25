s = input()

if len(s) > 4:
    s = s[0] + s[:-5:-1]
else:
    s = s[::-1]
print(int(s))
