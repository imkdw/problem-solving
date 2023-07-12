N = int(input())
call_time = map(int, input().split())

y_price, m_price = 0, 0
for i in call_time:
    y_price += (i // 30 + 1) * 10
    m_price += (i // 60 + 1) * 15

if y_price > m_price:
    print("M", m_price)
elif y_price < m_price:
    print("Y", y_price)
elif y_price == m_price:
    print("Y M", m_price)
