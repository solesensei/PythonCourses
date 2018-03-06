import math


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def ReduceFraction(n, m):
    g = gcd(n, m)
    return n / g, m / g


def main():
    n = int(input())
    m = int(input())
    p, q = ReduceFraction(n, m)
    print(int(p), int(q))

if __name__ == "__main__":
    main()
