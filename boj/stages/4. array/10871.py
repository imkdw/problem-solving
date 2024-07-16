n, x = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for num in nums:
    if num < x:
        print(num, end=" ")
