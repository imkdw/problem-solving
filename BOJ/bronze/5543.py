sangduk = int(input())
jungduk = int(input())
haduk = int(input())
cola = int(input())
sprite = int(input())

burger = [sangduk, jungduk, haduk]
drink = [cola, sprite]

result = burger[0] + drink[0]

for b in burger:
    for d in drink:
        cost = b + d
        if result > cost:
            result = cost

print(result - 50)
