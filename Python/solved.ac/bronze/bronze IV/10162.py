# 작성중인 코드 / 22.01.19

need_sec = int(input())
a, b, c = 300, 60, 10
a_cnt, b_cnt, c_cnt = 0, 0, 0
left_sec = 0
if need_sec >= a:
    a_cnt += need_sec // a
    left_sec = need_sec - a_cnt * a
    if left_sec >= b:
        b_cnt += left_sec // b
        left_sec -= b_cnt * b
        if left_sec >= c:
            c_cnt += left_sec // c
            if left_sec > 0:
                print(-1)

elif need_sec >= b:
    b_cnt += left_sec // b
    left_sec -= b_cnt * b
    if left_sec >= c:
        c_cnt += left_sec // c
        if left_sec > 0:
            print(-1)

elif need_sec >= c:
    c_cnt += left_sec // c
    if left_sec > 0:
        print(-1)

print(a_cnt, b_cnt, c_cnt)
