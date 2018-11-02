import math


def SeqSum(s):
    q = int(input())
    if q == 0:
        return s+q
    return SeqSum(s+q)


def main():
    s = SeqSum(0)
    print(s)

if __name__ == "__main__":
    main()
