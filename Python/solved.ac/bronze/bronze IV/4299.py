def solution(plus, minus):
    for i in range(plus):
        a, b = i, plus - i
        if a + b == plus and a - b == minus:
            return map(str, [a, b])
    return -1


plus, minus = map(int, input().split())
print(-1 if solution(plus, minus) == -1 else ' '.join(solution(plus, minus)))
