p = float(input())  # %
x = float(input())  # rub
y = float(input())  # kop

# to kop
y += x*100
y += int(y * p / 100)
# to rub kop
x = y // 100
y = y % 100

print('{:g} {:g}'.format(x, y))
