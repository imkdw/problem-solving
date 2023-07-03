N, B = map(str, input().split())
alpha = {}
result = 0
for i in range(0, 36):
    if i < 10:
        alpha[str(i)] = i
    else:
        alpha[chr(i + 55)] = i

for i in range(len(N)):
    value = alpha[N[i].upper()] * (int(B) ** (len(N) - i - 1))
    result += value

print(result)
