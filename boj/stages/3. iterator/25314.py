n = int(input())
count = n // 4
namuji = n % 4
for i in range(count):
    print("long", end=" ")

if namuji:
    print("long", end=" ")

print("int")
