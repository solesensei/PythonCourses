

def main():
    s, n = map(int, input().split())  # free space and users num
    users = []
    for i in range(n):
        users.append(int(input()))
    users.sort()
    count = -1
    while s > 0:
        count += 1
        if count == n:
            break
        s -= users[count]
    print(count)


if __name__ == "__main__":
    main()
