n = int(input())
result = 0
for _ in range(n):
    check = []
    s = input()
    is_group_word = True
    for i in s:
        if i in check:
            if check[-1] != i:
                is_group_word = False

        check.append(i)

    if is_group_word:
        result += 1

print(result)
