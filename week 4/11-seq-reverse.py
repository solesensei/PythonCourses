import math


def SeqReverse(q):
    q = int(input())
    if q == 0:
        print(0)
        return q
    SeqReverse(q)
    print(q)


def main():
    SeqReverse(0)

if __name__ == "__main__":
    main()
