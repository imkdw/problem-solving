x = int(input())
n = int(input())
amount = 0
for i in range(n):
    a, b = map(int, input().split())
    amount += a * b

if x == amount:
    print("Yes")
else:
    print("No")
