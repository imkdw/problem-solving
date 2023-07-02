data = [[0 for _ in range(100)] for _ in range(100)]
a = int(input())
result = 0
for i in range(a):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            data[j][k] += 1
            if data[j][k] == 1:
                result += 1

print(result)
