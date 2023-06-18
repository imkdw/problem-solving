scores = []
result = []
for i in range(28):
    score = input()
    scores.append(int(score))

for j in range(30):
    if j + 1 not in scores:
        result.append(j + 1)
print("\n".join(map(str, result)))