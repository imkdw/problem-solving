import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input() for _ in range(n)]
res = n * m


def ch(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] == chess[x + i][y + j]:
                cnt += 1
    return min(cnt, 64 - cnt)


for i in range(n - 7):
    print(f"i: {i}")
    for j in range(m - 1):
        print(f"j: {j}")
    print()
    # res = min(res, ch(i, j))
print(res)
