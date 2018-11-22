
# parametric iterator 

def turtle(cord, direction):
    tpos = cord
    tdir = direction
    walk = yield tpos
    while walk:
        if walk == 'f':
            if tdir == 0:
                tpos = (tpos[0] + 1, tpos[1])
            elif tdir == 1:
                tpos = (tpos[0], tpos[1] + 1)
            elif tdir == 2:
                tpos = (tpos[0] - 1, tpos[1])
            else:
                tpos = (tpos[0], tpos[1] - 1)
        elif walk == 'r':
            tdir = tdir - 1 if tdir > 0 else 3
        else:
            tdir = tdir + 1 if tdir < 3 else 1
        walk = yield tpos




robo = turtle((0,0),0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))

