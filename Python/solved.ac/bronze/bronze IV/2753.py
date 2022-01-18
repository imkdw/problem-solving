# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

year = int(input())
if not year % 4 and (year % 100 or not year % 400):
    print(1)
else:
    print(0)