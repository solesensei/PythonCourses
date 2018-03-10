mlist = list(map(int, input().split()))
pos_num = 0
for i in mlist:
    if i > 0:
        pos_num += 1
print(pos_num)
