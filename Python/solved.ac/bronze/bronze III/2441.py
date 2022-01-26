n = int(input())
for i in range(n, 0, -1):
    space = n - i
    print(' ' * space, '*' * i, sep='')