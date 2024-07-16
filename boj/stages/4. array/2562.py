nums = []
for i in range(9):
    num = int(input())
    nums.append(num)

print(max(nums), nums.index(max(nums)) + 1)
