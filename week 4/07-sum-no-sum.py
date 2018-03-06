import math


def ssum(a, b):
    s = 0
    if a == 0:
        return b
    if a < 0:
        s += ssum(a+1, b) - 1
    else:
        s += ssum(a-1, b) + 1
    return s


def main():
    a = int(input())
    b = int(input())
    print(ssum(a, b))

if __name__ == "__main__":
    main()
