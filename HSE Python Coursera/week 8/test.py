with open('test', "wb") as tst:
    for i in range(10):
        tst.write(bytes(i))
