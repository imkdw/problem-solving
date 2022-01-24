N, T, C, P = map(int, input().split())
seed_cnt = 0
for i in range(1, N + 1, T):
    if i == 1:
        seeding_cnt = C
        continue

    seed_cnt += seeding_cnt

print(seed_cnt * P)