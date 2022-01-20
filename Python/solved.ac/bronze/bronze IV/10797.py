day = int(input())
cars = list(map(int, input().split()))
cnt = 0
for car in cars:
    if day == car:
        cnt += 1
print(cnt)