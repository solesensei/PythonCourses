import math


# Get maximum prime < N 
def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def MaxPrime(n):
    for i in range(n,1,-1):
        if isPrime(i):
            return i
    return 2

def main():
    n = int(input())
    print(MaxPrime(n))

if __name__ == "__main__":
    main()