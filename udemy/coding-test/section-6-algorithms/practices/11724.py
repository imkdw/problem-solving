# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
node_count, edge_count = map(int, input().split())

# 인접행렬 생성
adj = [[0] * node_count for _ in range(node_count)]
for _ in range(edge_count):
    start, end = map(lambda x: x - 1, map(int, input().split()))
    adj[start][end] = adj[end][start] = 1

# 요소개수
result = 0

# 노드 방문여부 체크용 배열
chk = [False] * node_count


def dfs(now):
    for nxt in range(node_count):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(node_count):
    if not chk[i]:
        result += 1
        chk[i] = True
        dfs(i)

print(result)