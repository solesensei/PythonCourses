# Drawing sauare with symbols

def print_p(f):
    for s in f:
        print(*s)


def squares(n,m, *square):
    field = [['.' for i in range(n)] for j in range(m)]
    for sq in square:
        for i in range(sq[2]):
            for j in range(sq[2]):
                field[sq[1] + i][sq[0] + j] = sq[3] 
    for s in field:
        for k in s:
            print(k,sep='', end='')
        print()

# squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))
