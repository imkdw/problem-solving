N = int(input())
max = N * 2 - 1

for i in range(N):
    space = max // 2
    print(' ' * space, end="")
    print('*' * ((i * 2) - 1))
    print(' ' * space, end="")
