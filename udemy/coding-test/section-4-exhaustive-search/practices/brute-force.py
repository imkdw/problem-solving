"""
N개의 입력값 중 2개의 쌍이 제일 큰 경우
"""

import sys

input = sys.stdin.readline


def n_2():
    """
        O(N^2)의 방법
    """
    max_1 = 0
    max_2 = 0

    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                max_1 = numbers[i]
                max_2 = numbers[j]
            elif numbers[i] < numbers[j]:
                max_1 = numbers[j]
                max_2 = numbers[i]
            else:
                max_1 = numbers[i]
                max_2 = numbers[j]
    print(max_1 + max_2)


def n_log_n():
    """
        O(N log N)의 방법
    """
    n = int(input())
    numbers = sorted([int(input()) for _ in range(n)], reverse=True)
    print(numbers[0] + numbers[1])


n_log_n()
