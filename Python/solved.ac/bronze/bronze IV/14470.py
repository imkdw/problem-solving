a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0

if a < 0:
    time += d
    for _ in range(a, 0):
        time += 1 * c
    a = 0
for _ in range(a, b):
    time += 1 * e

print(time)