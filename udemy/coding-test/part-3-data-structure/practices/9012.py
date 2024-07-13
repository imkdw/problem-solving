# https://www.acmicpc.net/problem/9012

for _ in range(int(input())):
    stack = []
    isVPS = True

    for char in input():
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break

    if stack:
        isVPS = False

    print("YES" if isVPS else "NO")