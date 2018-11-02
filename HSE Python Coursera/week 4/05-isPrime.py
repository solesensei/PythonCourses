import math


def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    n = int(input())
    if isPrime(n):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
