arr = []
for i in range(9):
    s = input()
    arr.append(list(map(int, s.split())))

max_num = 0
pos_a, pos_b = 0, 0
for i_idx, i in enumerate(arr):
    for j_idx, j in enumerate(i):
        if j > max_num:
            max_num = j
            pos_a, pos_b = i_idx, j_idx
print(max_num)
print(pos_a + 1, pos_b + 1)
