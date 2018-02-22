n = int(input())

left = n // 100
right = n % 100
reverse_left = left % 10 * 10 + left // 10

print(reverse_left - right + 1)
