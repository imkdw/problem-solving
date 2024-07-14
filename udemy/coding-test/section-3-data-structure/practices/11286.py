# https://www.acmicpc.net/problem/11286

import heapq
import sys

input = sys.stdin.readline


N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
