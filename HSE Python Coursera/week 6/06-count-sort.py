

def CountSort(A):
    less = []
    equal = []
    greater = []

    if len(A) > 1:
        pivot = A[0]
        for x in A:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return CountSort(less)+equal+CountSort(greater)
    else:
        return A


def main():
    inList = list(map(int, input().split()))
    print(' '.join(map(str, CountSort(inList))))

if __name__ == "__main__":
    main()
