abcd_list = []
ef_list = []
for _ in range(4):
    abcd_list.append(int(input()))
for _ in range(2):
    ef_list.append(int(input()))
abcd_list, ef_list = list(reversed(sorted(abcd_list))), list(reversed(sorted(ef_list)))
print(abcd_list[0] + abcd_list[1] + abcd_list[2] + ef_list[0])