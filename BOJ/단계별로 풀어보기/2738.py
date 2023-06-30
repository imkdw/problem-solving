numbers = input().split()
N, M = int(numbers[0]), int(numbers[1])
items = []

for i in range(N * 2):
    a = list(map(int, input().split()))
    items.append(a)

for i in range(min(len(items), N)):
    for j in range(len(items[i])):
        print(items[i][j] + items[i + N][j], end=" ")
    print()
