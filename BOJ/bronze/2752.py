nums = list(map(int, input().split()))
nums.sort()
nums = [str(num) for num in nums]
print(' '.join(nums))