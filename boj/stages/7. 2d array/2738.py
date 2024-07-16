import sys

input = sys.stdin.readline

arr1, arr2 = [], []
n, m = map(int, input().split())

for _ in range(n):
    s = input().split()
    arr1.append(list(map(int, s)))

for _ in range(n):
    s = input().split()
    arr2.append(list(map(int, s)))

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end=' ')
    print()