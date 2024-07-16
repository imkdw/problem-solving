# https://www.acmicpc.net/problem/10813
n, m = map(int, input().split())

baskets = []
for _ in range(n):
    baskets.append(_ + 1)

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    baskets[i], baskets[j] = baskets[j], baskets[i]

print(*baskets)
