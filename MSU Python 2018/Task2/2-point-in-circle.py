# check if point in circle
def check(c, x):
    if x == (0,0):
        return True
    in_c = (x[0] - c[0]) ** 2 + (x[1] - c[1]) ** 2 <= c[2]**2
    ans = check(c, eval(input())) and in_c
    return ans
    # return inC

circle = eval(input())

x = eval(input())
ans = check(circle, x)
if ans:
    print('YES')
else:
    print('NO')