arr = []
while True:
    s = input()
    if s == '':
        break
    arr.append(s.split())

for a in range(len(arr)):
    print(a)
    print(arr[a][0][0])
