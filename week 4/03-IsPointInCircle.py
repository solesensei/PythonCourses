def IsPointInCircle(x, y, xc, yc, r):
    return (xc - x)**2 + (yc - y)**2 - r**2 <= 0.0001


def main():
    x = float(input())
    y = float(input())
    xc = float(input())
    yc = float(input())
    r = float(input())
    if IsPointInCircle(x, y, xc, yc, r):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
