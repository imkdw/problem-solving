minguk = list(map(int, input().split()))
mansae = list(map(int, input().split()))
big_score = sum(minguk) if sum(minguk) > sum(mansae) else sum(mansae)
print(big_score)