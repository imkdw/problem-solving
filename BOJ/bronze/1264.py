moum = ['a', 'e', 'i', 'o', 'u']
while(True):
    count = 0
    word = input().lower()
    if word == '#':
        break;
    for i in word:
        if i in moum:
            count += 1
    print(count)