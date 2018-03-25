n = int(input())
m = n * 100 + 99
count = 0
for i in range(m + 1):
    if i <= 101:
        continue
    s = str(i)
    if (s[0] != s[1] and s[0] != s[2] and s[1] != s[2] and
            int(s[1]) != 5 and int(s[2]) % 2 == 0):
            count += 1
print(count)
