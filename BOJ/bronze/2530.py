hour, min, second = map(int, input().split())
plus_second = int(input())

min += plus_second // 60
second += plus_second % 60

if second >= 60:
    min += second // 60
    second = second % 60

if min >= 60:
    hour += min // 60
    min = min % 60

if hour >= 24:
    hour %= 24

print(hour, min, second)


