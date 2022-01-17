hours, minutes = map(int, input().split())
need_time = int(input())

after_hours = hours + ((minutes + need_time) // 60)
after_min = (minutes + need_time) - ((minutes + need_time) // 60 * 60)
after_hours = 0 + (after_hours - 24) if after_hours >= 24 else after_hours
print(after_hours, after_min)