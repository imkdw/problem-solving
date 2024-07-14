"""
집합 Set
- 삽입/삭제 : O(1)
- 탐색 : O(1)
"""

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)  # {1, 2, 3}

s.add(1)
print(s)  # {1, 2, 3}