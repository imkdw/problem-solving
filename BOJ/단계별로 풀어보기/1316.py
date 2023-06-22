N = int(input())
data = []
is_group = True
group = 0
for i in range(N):
    word = input()
    for j in range(len(word)):
        if j == len(word) - 1:
            if word[j] in data:
                is_group = False
            break

        if word[j] != word[j + 1]:
            if word[j] in data:
                is_group = False
            data.append(word[j])
    if is_group:
        group += 1

    data = []
    is_group = True



print(group)
