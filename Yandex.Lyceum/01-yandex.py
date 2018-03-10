def isPolyndrom(s):
    revers = s[::-1]
    if s == revers:
        print('YES')
    else:
        print('NO')

n = int(input())
i = 0
while i < n:
    s = input()
    s = s.lower()
    s = s.replace('ё', 'е')
    k = 0
    tmp = ''
    while k < len(s):
        if s[k].isalpha():
            tmp += s[k]
        k += 1
    s = tmp
    isPolyndrom(s)
    i += 1
