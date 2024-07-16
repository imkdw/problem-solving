# https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())
rh, rm = h, 0


if m - 45 < 0:
    rm = m - 45 + 60
    rh -= 1
else:
    rm = m - 45

if rh < 0:
    rh = rh + 24

print(rh, rm)
