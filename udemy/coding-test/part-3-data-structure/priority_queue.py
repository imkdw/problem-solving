"""
우선순위 큐 Priority Queue
- 삽입/삭제 : O(logN)
- 탐색 : O(1)

heapq 기준 파이썬은 min-heap 제공

from queue import PriorityQueue
PriorityQueue의 경우 thread-safe 기능을 제공해서 느림
"""

import heapq

pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)
print("size:", len(pq))  # 3
while len(pq) > 0:
    print(heapq.heappop(pq))  # 789
