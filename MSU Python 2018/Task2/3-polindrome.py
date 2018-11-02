# palindrome
def palindrome(n, rn):
    if n == 0:
        return rn
    rn = rn * 10 + n % 10
    n //= 10
    return palindrome(n, rn)

num = int(input())
a = palindrome(num, 0)
if a == num:
    print('YES')
else:
    print('NO')
