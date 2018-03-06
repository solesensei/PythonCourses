def min4(a, b, c, d):
    ab = min(a, b)
    cd = min(c, d)
    return min(ab, cd)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(min4(a, b, c, d))

if __name__ == "__main__":
    main()
