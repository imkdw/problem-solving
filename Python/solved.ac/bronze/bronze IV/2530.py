hours, minutes, seconds = map(int, input().split())
cook_seconds = int(input())

# 3600초 이상 걸리면 시/분/초로 나눠야함
if cook_seconds >= 3600:
    after_hours = cook_seconds // 3600
    after_minutes = cook_seconds // 3600 // 60
    after_seconds = cook_seconds // 3600 % 60
    print(after_hours, after_minutes, after_seconds)
    # print(hours + after_hours, minutes + after_minutes, seconds + after_seconds)
else:
    after_minutes = cook_seconds // 60
    after_seconds = cook_seconds % 60
    print(after_minutes, after_seconds)
    # print(hours, minutes + after_minutes, seconds + after_seconds)


