# Look Say generator

def LookSay():
    n = 1
    L = []
    l = [1]
    s = ''
    y = ''
    while True:
        x = str(l[n - 1]) + ' '
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]: 
                s += 1
            else:
                y += str(s)+  str(x[i])
                s = 1
        x = ''
        n += 1       
        l += [int(y), ]
       
        for j in range(len(y)):
            yield int(y[j])
        y = ''
        s = 1

# for i, l in enumerate(LookSay()):
    # print(f"{i}: {l}")
    # if i > 15:
        # break

# from itertools import groupby
# def LookSay():
#     s = '1'
#     yield s
#     while True:
#         s = ''.join(str(len(list(group))) + key for key, group in groupby(s))
#         for i in s:
#             yield i
