import sys
a = int(sys.stdin.readline())

if a == 1:
    print(4)
else:
    print((a * 3 + 1) + int(0.5 * (a * 2 - 1)))