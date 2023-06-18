X = int(input())  # 영수증 총 가격
N = int(input())  # 구매한 물건 종류(갯수)
result = 0
for i in range(N):
   a, b = map(int, input().split())
   result += a * b

if (X == result):
    print('Yes')
else:
    print('No')