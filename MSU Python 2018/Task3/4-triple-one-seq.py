# zeros ones sequence count where 3 '1' not together (111) triple one

def triple_one(n):
    f = {}
    f[1] = 2
    f[2] = 4
    f[3] = 7
    for i in range(4,n+1):
        f[i] = f[i-1] + f[i-2] + f[i-3] 
    return f[n]

n = int(input())
count = triple_one(n)
print(count)
