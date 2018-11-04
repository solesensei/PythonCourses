# Look Say generator
from itertools import groupby


def LookSay():
    s = '1'
    yield s
    while True:
        s = ''.join(str(len(list(group))) + key for key, group in groupby(s))
        for i in s:
            yield i

# for i, l in enumerate(LookSay()):
    # print(f"{i}: {l}")
    # if i > 15:
    #     break
