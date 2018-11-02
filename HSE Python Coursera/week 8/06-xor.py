print(*map(
    lambda i: int(i[0] != i[1]),
    zip(
        map(
            int, input().split()
        ),
        map(
            int, input().split()
        )
    )
    )
)
