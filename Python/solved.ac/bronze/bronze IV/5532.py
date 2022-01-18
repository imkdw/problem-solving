vacation = int(input())
math = int(input())
korean = int(input())
korean_day = int(input())
math_day = int(input())

korean_time, math_time = korean // korean_day, math // math_day

if korean % korean_day:
    korean_time += 1

if math % math_day:
    math_time += 1

print(vacation - max(korean_time, math_time))
