N, M = map(int, input().split())
ball = [i+1 for i in range(N)]
for i in range(M):
    i, j = map(int, input().split())
    temp_arr = ball[i-1:j]
    reversed_temp_arr = list(reversed(temp_arr))
    ball[i-1:j] = reversed_temp_arr
print(" ".join(map(str, ball)))
