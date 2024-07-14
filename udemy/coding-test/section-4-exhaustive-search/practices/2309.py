# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

input = sys.stdin.readline

all_dwarf = 9
correct_dwarf = 7
correct_drawfs_height = 100

drawfs_height = [int(input()) for _ in range(all_dwarf)]
for i in combinations(drawfs_height, correct_dwarf):
    if sum(i) == correct_drawfs_height:
        print('\n'.join(map(str, sorted(i))))
        break
