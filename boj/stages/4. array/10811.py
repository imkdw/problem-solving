# https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
baskets = [_ for _ in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1

    baskets[i:j] = baskets[i:j][::-1]

print(*baskets)
