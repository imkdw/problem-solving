k, n, m = map(int, input().split())
need_price = abs(m - k * n) if m - k * n < 0 else 0
print(need_price)