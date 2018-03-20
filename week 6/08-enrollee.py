class Man:
    name = ''
    surname = ''
    score = 0


def manSort(man):
    return -man.score


def main():
    inFile = open("input.txt", 'r', encoding='utf8')
    outFile = open("output.txt", 'w', encoding='utf8')
    people = []
    lines = inFile.readlines()
    k = int(lines[0])
    for line in lines[1:]:
        tmp = line.split()
        man = Man()
        man.surname = tmp[0]
        man.name = tmp[1] + (' ' + tmp[2] if tmp[2].isalpha() else '')
        man.score = int(tmp[-1]) + int(tmp[-2]) + int(tmp[-3])
        if not (int(tmp[-1]) < 40 or int(tmp[-2]) < 40 or int(tmp[-3]) < 40):
            people.append(man)
    people.sort(key=manSort)
    score = people[0].score
    if k >= len(people):
        print(0, file=outFile)
    elif people[k].score == people[0].score:
        print(1, file=outFile)
    elif people[k].score != people[k-1].score:
        print(people[k-1].score, file=outFile)
    else:
        for man in people:
            if people[k-1].score == man.score:
                break
            score = man.score
        print(score, file=outFile)

    inFile.close()
    outFile.close()

if __name__ == "__main__":
    main()
