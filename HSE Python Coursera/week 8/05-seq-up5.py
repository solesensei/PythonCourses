from functools import reduce


print(
    reduce(
        lambda a, b: a * b,
        map(
            lambda x: x**5,
            map(int, input().split())
        )
    )
)
