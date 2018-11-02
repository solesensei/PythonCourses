l = []


def isFirstTime(s):
    global l
    if l.count(s):
        return False
    l.append(s)
    return True


def main():
    inFile = open("input.txt", 'r', encoding='utf8')
    outFile = open("output.txt", 'w', encoding='utf8')
    lines = inFile.readlines()
    count = 0
    for n, word in enumerate(lines):
        if (len(word) == 8 or len(lines)-1 == n) and isFirstTime(word):
            count += 1
            if count == 7:
                break
        print('ещё', file=outFile)
    print('всё!', file=outFile)
    inFile.close()
    outFile.close()


if __name__ == "__main__":
    main()
