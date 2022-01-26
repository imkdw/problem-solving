n = int(input())
all_star = 2 * n - 1
for i in range(1, all_star + 1, 2):
    space = (all_star - i) // 2
    print(' ' * space, '*' * i, sep='')
