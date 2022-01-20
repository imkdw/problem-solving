x_price = int(input())  # x사 1리터당 요금
y_price = int(input())  # y사 기본 요금
y_max = int(input())  # y사 최대 물 사용량
y_over_price = int(input())  # y사 오버시 1리터당 요금
use_water = int(input())  # 사용하는 물 총량

x_water_price = x_price * use_water
y_water_price = y_price if y_max > use_water else y_price + ((use_water - y_max) * y_over_price)
print(min(x_water_price, y_water_price))
