A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(' '.join(map(str, sorted(A & B))))
