a, b, c = map(int, input().split())
result = 0

# 3개의 눈이 모두 동일
if a == b == c:
    result = 10000 + a * 1000
# 2개의 눈이 동일
elif a == b or a == c or b == c:
    same_num = 0
    if a == b:
        same_num = a
    elif a == c:
        same_num = a
    elif b == c:
        same_num = b
    result = 1000 + same_num * 100
# 같은 눈이 없을때
else:
    max_num = max(a, b, c)
    result = max_num * 100

print(result)
