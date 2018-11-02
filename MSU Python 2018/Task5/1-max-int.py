# Maximum integer in string


a = input().split()
first = True
s = 0
while a:
    for elem in a:
        if elem.isdigit():
            if first:
                s = int(elem)
                first = False
            if int(elem) > s:
                s = int(elem)
    a = input().split()
print(s)