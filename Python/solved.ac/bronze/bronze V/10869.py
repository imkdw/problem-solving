a, b = map(int, input().split())
sep = [a + b, a - b, a * b, a // b, a % b]
for _ in sep:
    print(_)