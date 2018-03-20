class Man():
    name = ''
    score = 0


def manSort(man):
    return -man.score


def main():
    n = int(input())
    people = []
    for i in range(n):
        tmp = input().split()
        man = Man()
        man.name = tmp[0]
        man.score = int(tmp[1])
        people.append(man)
    people.sort(key=manSort)
    for man in people:
        print(man.name)

if __name__ == "__main__":
    main()
