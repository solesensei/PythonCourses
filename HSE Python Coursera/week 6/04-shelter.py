def numerate_list(l, n):
    tmp = []
    for i in range(n):
        tmp.append(tuple((l[i], i)))
    return tmp


def main():
    n = int(input())
    towns = list(map(int, input().split()))
    m = int(input())
    shelters = list(map(int, input().split()))

    towns = numerate_list(towns, n)
    shelters = numerate_list(shelters, m)
    towns.sort()
    shelters.sort()
    s = 0
    i = 0
    res = [1 for i in range(n)]
    while i < n:
        if s < m-1:
            t = towns[i][0]
            s1 = shelters[s][0]
            s2 = shelters[s+1][0]
            if t <= s1:
                res[towns[i][1]] = shelters[s][1]+1
            elif t <= s2:
                dist_left = abs(t - s1)
                dist_right = abs(t - s2)
                if dist_left <= dist_right:
                    res[towns[i][1]] = shelters[s][1]+1
                else:
                    res[towns[i][1]] = shelters[s+1][1]+1
            else:
                s += 1
                i -= 1
        else:
            res[towns[i][1]] = shelters[m-1][1]+1
        i += 1
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
