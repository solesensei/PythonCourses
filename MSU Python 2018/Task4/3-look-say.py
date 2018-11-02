# Look Say generator

def LookSay():
    ps = '1'
    yield ps
    while 1:
        s = ''
        d = list(ps)[0]
        k = 0
        for i in list(ps):
            if d != i:
                s += str(k) + str(d)
                d = i
                k = 0
            k += 1
        s += str(k) + str(d)
        ps = s
        for i in list(s):
            yield i


# for i,l in enumerate(LookSay()):
#     print(f"{i}: {l}")
#     if i>10:
#         break