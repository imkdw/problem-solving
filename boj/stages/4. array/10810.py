# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
baskets = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i - 1, j):
        baskets[a] = k

print(*baskets)
