"""
대기열 Queue
- 삽입/삭제 : O(1)
- 탐색 : O(1)

from queue import Queue
Queue의 경우 thread-safe 기능을 제공해서 느림
"""

from collections import deque


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())  # 1
print(q.popleft())  # 2
print(q.popleft())  # 3