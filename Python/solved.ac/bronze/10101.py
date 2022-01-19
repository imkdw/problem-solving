gaks = []
for _ in range(3):
    gaks.append(int(input()))

if sum(gaks) == 180:
    if len(set(gaks)) == 1:
        print('Equilateral')
    elif len(set(gaks)) == 2:
        print('Isosceles')
    elif len(set(gaks)) == 3:
        print('Scalene')
else:
    print('Error')