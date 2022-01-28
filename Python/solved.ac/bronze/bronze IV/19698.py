N, W, H, L = map(int, input().split())

a = W // L
b = H // L
result = a * b

print(N if N < result else result)
