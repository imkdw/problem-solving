# https://www.acmicpc.net/problem/10815

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
card_num = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

result = []

for num in nums:
    l = bisect_left(card_num, num)
    r = bisect_right(card_num, num)
    result.append(1 if r - l else 0)

print(' '.join(map(str, result)))
