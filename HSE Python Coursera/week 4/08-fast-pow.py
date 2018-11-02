import math


def fastpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fastpow(a**2, n/2)
    else:
        return a*fastpow(a, n-1)


def main():
    a = float(input())
    n = int(input())
    print(fastpow(a, n))

if __name__ == "__main__":
    main()
