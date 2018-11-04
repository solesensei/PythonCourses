# Maximum integer in string


string = input().split()
first = True
max_elem = 0
while string:
    for elem in string:
        if elem.isdigit() or elem[0] == '-' and elem[1:].isdigit():
            if first:
                max_elem = int(elem)
                first = False
            if int(elem) > max_elem:
                max_elem = int(elem)
    string = input().split()
print(max_elem)
