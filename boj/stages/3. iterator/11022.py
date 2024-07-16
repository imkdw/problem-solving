t = int(input())
results = []
for _ in range(t):
    n, m = list(map(int, input().split()))
    results.append([n, m])

for idx, result in enumerate(results):
    print(f"Case #{idx+1}: {result[0]} + {result[1]} = {result[0] + result[1]}")
