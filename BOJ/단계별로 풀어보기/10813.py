# N : 총 가지고있는 바구니
# M : 앞으로 M번 공을 바꾼다는 뜻
N, M = map(int, input().split())
ball = [i + 1 for i in range(N)]
for i in range(M):
    i, j = map(int, input().split())
    ball[i - 1], ball[j - 1] = ball[j - 1], ball[i - 1]
print(" ".join(map(str, ball)))