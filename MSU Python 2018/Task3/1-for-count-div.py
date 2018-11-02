# moar((25,0,-115,976,100500,7),(32,5,78,98,10,9,42),5)
# for count, check if a has more devisible members to n than b
def moar(a,b,n):
    count_a = 0
    count_b = 0
    for elem in a:
        if elem % n == 0:
            count_a += 1
    for elem in b:
        if elem % n == 0:
            count_b += 1
    return count_a > count_b
