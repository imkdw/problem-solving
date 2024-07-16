nums = [int(input()) for _ in range(10)]
result_arr = []
count = 0
for num in nums:
    n = num % 42
    if n not in result_arr:
        count += 1
        result_arr.append(n)

print(count)
