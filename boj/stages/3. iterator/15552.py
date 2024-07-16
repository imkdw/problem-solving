# https://www.acmicpc.net/problem/15552

import sys

input = sys.stdin.readline


t = int(input())
nums = []
for _ in range(t):
    nums.append(list(map(int, input().split())))

for num in nums:
    print(num[0] + num[1])
