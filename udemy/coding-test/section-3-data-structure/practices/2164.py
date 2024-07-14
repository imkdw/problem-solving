# https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())

desk = deque()
for _ in range(1, N+1 ):
    desk.append(_)

while len(desk) > 1:
    # 카드 한장 버리기
    desk.popleft()

    # 제일 위에 카드를 뒤로 옮기기
    top_card = desk.popleft()
    desk.append(top_card)

print(desk[0])
