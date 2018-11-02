s = input()

first = s.find('f')
second = s.rfind('f')

if first == second and first != -1:
    print(first)
elif first < second:
    print(first, second)
