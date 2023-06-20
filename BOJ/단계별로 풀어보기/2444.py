N = int(input())
star_cnt = 1
mid = N * 2 - 1
for i in range(N):
    space = (mid - star_cnt) // 2
    print(' ' * space + '*' * star_cnt)
    star_cnt += 2

for j in range(N):
    if j == 0:
        star_cnt -= 2
        continue
    star_cnt -= 2
    space = (mid - star_cnt) // 2
    print(' ' * space + '*' * star_cnt)
