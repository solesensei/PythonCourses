# Linear labyrinth: go from [0] to [-1]

def run_labyrinth(k, A, was_here):
    if k >= len(A) or k < 0 or k in was_here:
        return False
    was_here.add(k)
    if k == len(A) - 1:
        return True
    return run_labyrinth(k+A[k], A, was_here) or run_labyrinth(k-1, A, was_here)

A = eval(input())
was_here = set()
passed = run_labyrinth(0, A, was_here)
if passed:
    print('YES')
else:
    print('NO')
