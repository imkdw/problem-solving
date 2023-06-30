nums = []
max_num = 0
pos1 = 0
pos2 = 0

for i in range(9):
    num = map(int, input().split())
    nums.append(list(num))

for i in range(len(nums)):
    if max_num < max(nums[i]):
        max_num = max(nums[i])
        pos1 = i
        pos2 = nums[i].index(max_num)

print(max_num)
print(pos1 + 1, pos2 + 1)
