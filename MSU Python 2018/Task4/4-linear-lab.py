# Linear labyrinth: go from [0] to [-1]

def run_labyrinth(A, was_here):
    part = A[0] if A[0] < len(A) else -1
    k = 0
    while k <= part:
        if A[k] + k == len(A) - 1:
            return True
        if part < A[k] + k and A[k] + k < len(A):
            part = A[k] + k
        k += 1
    return False

A = eval(input())
was_here = set()
passed = run_labyrinth(A, was_here)
if passed:
    print('YES')
else:
    print('NO')


# recursion
# def run_labyrinth_rec(k, A, was_here):
#     if k >= len(A) or k < 0 or k in was_here:
#         return False
#     was_here.add(k)
#     if k == len(A) - 1:
#         return True
#     return run_labyrinth(k+A[k], A, was_here) or run_labyrinth(k-1, A, was_here)
