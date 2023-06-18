# N : 총 바구니 갯수
# M : 앞으로 공을 넣을 횟수
N, M = map(int, input().split())
ball = [0] * N
for i in range(M):
    # i ~ j번 바구니까지 k번 공을 넣음
    i, j, k = map(int, input().split())
    for a in range(i, j + 1):
        ball[a - 1] = k
print(" ".join(map(str, ball)))