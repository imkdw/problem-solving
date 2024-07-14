# https://www.acmicpc.net/problem/2512

import sys

input = sys.stdin.readline

# 지방의 수, 3 <= n <= 10000
city_count = int(input())

# 지방에서 요청하는 예산금액, 1 <= x <= 100000
req_money = list(map(int, input().split()))

# 총 예산, n <= m <= 10^10
all_money = int(input())

low = 0
high = max(req_money)
mid = (low + high) // 2
result = 0


# 국가 총 예산으로 감당이 가능한지
def is_possible(mid: int) -> bool:
    return sum(min(r, mid) for r in req_money) <= all_money


while low <= high:
    if is_possible(mid):
        low = mid + 1
        result = mid
    else:
        high = mid - 1

    mid = (low + high) // 2

print(result)
