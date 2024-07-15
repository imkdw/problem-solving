"""
피보나치에선 0보다 크거나 같은 숫자가 등장
초기값으로 음수를 넣어서 이미 한번 계산했는지 검증하기 위함
"""

cache = [-1] * 91
cache[0] = 0
cache[1] = 1


def f(n: int) -> int:
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]


print(f(int(input())))
