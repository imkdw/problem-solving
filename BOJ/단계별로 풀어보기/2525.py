hour, min = map(int, input().split())
plus_min = int(input())

# 분을 더하고 초과한 분을 계산
min += plus_min
hour += min // 60
min = min % 60

if hour >= 24:
    temp_hour = 0
    hour = temp_hour + hour % 24
print(hour, min)