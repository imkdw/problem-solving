dice_list = list(map(int, input().split()))
max_dice = {}
for dice in dice_list:
    max_dice[dice_list.count(dice)] = dice

max_dice_num = max(max_dice.keys())
max_dice_value = max_dice[max_dice_num]

if max_dice_num == 3:
    print(10000 + max_dice_value * 1000)
elif max_dice_num == 2:
    print(1000 + max_dice_value * 100)
else:
    print(max(dice_list) * 100)