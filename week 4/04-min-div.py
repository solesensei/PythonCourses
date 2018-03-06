import math


def MinDivisor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i
        i += 1
    return n


def main():
    n = int(input())
    print(MinDivisor(n))


if __name__ == "__main__":
    main()
