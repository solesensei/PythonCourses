def merge(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        C += A[i:]
    elif j < len(B):
        C += B[j:]
    return C


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(' '.join(map(str, merge(A, B))))

if __name__ == "__main__":
    main()
