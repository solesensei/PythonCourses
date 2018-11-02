# spital digits matrix 

def print_matrix(m):
    for e in m:
        print(*e)


def fill_row(m,a,b,n):
    k = 1 if b > a else -1
    for i in range(a,b,k):
        m[i] = n % 10
        n += 1
    return n

def fill_col(m,col,a,b,n):
    k = 1 if b > a else -1
    for i in range(a,b,k):
        m[i][col] = n % 10
        n += 1
    return n

def spiral(m,n):
    matrix = [[0 for i in range(n)] for j in range(m)]
    k = 0
    left = 0
    right = n-1
    up = 0
    down = m-1
    while right-left >= 0 and down-up >= 0:
        k = fill_row(matrix[up], left, right+1, k)
        up += 1
        if right-left < 0 or down-up < 0: break
        k = fill_col(matrix, right, up, down+1, k)
        right -= 1
        if right-left < 0 or down-up < 0: break
        k = fill_row(matrix[down], right, left-1, k)
        down -= 1
        if right-left < 0 or down-up < 0: break
        k = fill_col(matrix, left, down, up-1, k)
        left += 1
    return matrix

n,m = eval(input())
mtx = spiral(m,n)
print_matrix(mtx)
