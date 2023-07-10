N = int(input())
call_time = map(int, input().split())
for i in call_time:
    y_price = i // 30 * 10 + 10
    m_price = i // 60 * 15 + 15
    print(y_price, m_price)


