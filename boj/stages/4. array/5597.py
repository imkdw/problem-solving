all_nums = set([int(_) for _ in range(1, 31)])
given_nums = set([int(input()) for _ in range(28)])
result = sorted(list(all_nums - given_nums))

for r in result:
    print(r)
