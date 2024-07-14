# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

coin_count, target_price = map(int, input().split())
coins = [int(input()) for _ in range(coin_count)]

coin_count = 0
for coin in sorted(coins, reverse=True):
    if target_price <= 0:
        break

    if target_price // coin > 0:
        need_coin_count = target_price // coin
        target_price = target_price % coin
        coin_count += need_coin_count

print(coin_count)


