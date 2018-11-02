# 12345
# generator 
def generator(n):
    yield -n
    yield str(n)
    n = -n if n < 0 else n
    yield n // 10 % 10
