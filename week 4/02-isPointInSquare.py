def isPointInSquare(x, y):
    return(-1 <= x <= 1 and -1 <= y <= 1)


def main():
    x = float(input())
    y = float(input())
    if isPointInSquare(x, y):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
