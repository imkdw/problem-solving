nums = map(int, input().split())
result = 0
for i in nums:
    result += i * i

print(result % 10)
