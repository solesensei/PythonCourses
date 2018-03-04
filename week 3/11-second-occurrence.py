s = input()

first = s.find('f')
second = s.find('f', first+1)

if first == -1:
    print(-2)
elif second == -1:
    print(-1)
else:
    print(second)
