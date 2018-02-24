a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())

box = -1  # 0 - equal, 1 - 1 > 2, 2 - 2 > 1

if (a <= x and b <= y and c <= z or
        a <= x and b <= z and c <= y or
        a <= y and b <= x and c <= z or
        a <= y and b <= z and c <= x or
        a <= z and b <= x and c <= y or
        a <= z and b <= y and c <= x):
    box = 2
elif (a >= x and b >= y and c >= z or
        a >= x and b >= z and c >= y or
        a >= y and b >= x and c >= z or
        a >= y and b >= z and c >= x or
        a >= z and b >= x and c >= y or
        a >= z and b >= y and c >= x):
    box = 1

if (a == x and b == y and c == z or
        a == x and b == z and c == y or
        a == y and b == x and c == z or
        a == y and b == z and c == x or
        a == z and b == x and c == y or
        a == z and b == y and c == x):
    box = 0

if box == 0:
    print('Boxes are equal')
elif box == 2:
    print('The first box is smaller than the second one')
elif box == 1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
