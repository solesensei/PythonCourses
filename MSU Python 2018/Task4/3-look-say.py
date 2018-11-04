# Look Say generator

def LookSay():
    ps = '1'
    yield ps
    while True:
        s = ''
        d = ps[0]
        k = 0
        for i in range(len(ps)):
            if d != ps[i]:
                s += str(k) + d
                d = ps[i]
                k = 0
            k += 1
        s += str(k) + d
        ps = s
        print(s)
        for i in range(len(s)):
            yield s[i]

# for i, l in enumerate(LookSay()):
#     print(f"{i}: {l}")
#     if i > 15:
#         break

# from itertools import groupby
# def LookSay():
#     s = '1'
#     yield s
#     while True:
#         s = ''.join(str(len(list(group))) + key for key, group in groupby(s))
#         for i in s:
#             yield i
