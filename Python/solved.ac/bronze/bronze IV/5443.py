burgers: list = []
drinks: list = []
for i in range(5):
    item = int(input())
    if i < 3:
        # 햄버거는 3개까지 burgers에 추가
        burgers.append(item)
    else:
        # 나머지는 음료에 추가
        drinks.append(item)
burgers.sort()
drinks.sort()
print(burgers[0] + drinks[0] - 50)