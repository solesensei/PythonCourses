a = int(input())
b = int(input())

print(b*(a % b == a) + a*(b % a == b) + a*(a % b == 0))
