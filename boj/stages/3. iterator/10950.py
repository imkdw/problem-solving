t = int(input())
nums = []
for _ in range(t):
    a, b = map(int, input().split())
    nums.append([a, b])

for num in nums:
    print(num[0] + num[1])
