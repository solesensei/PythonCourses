class Man:
    name = ''
    surname = ''
    score = 0


def manSort(man):
    return (man.surname, man.name)


def main():
    inFile = open("input.txt", 'r', encoding='utf8')
    outFile = open("output.txt", 'w', encoding='utf8')
    people = []
    for line in inFile:
        tmp = line.split()
        man = Man()
        man.surname = tmp[0]
        man.name = tmp[1]
        man.score = tmp[3]
        people.append(man)
    people.sort(key=manSort)
    for man in people:
        print(man.surname, man.name, man.score, end='\n', file=outFile)
    inFile.close()
    outFile.close()

if __name__ == "__main__":
    main()
