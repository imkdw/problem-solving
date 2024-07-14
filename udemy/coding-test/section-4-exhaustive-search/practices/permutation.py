"""
순열
"""
from itertools import permutations


def permutation():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    for i in permutations(numbers, 2):
        print(i)

permutation()