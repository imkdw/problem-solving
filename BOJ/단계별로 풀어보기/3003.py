complete_pieces = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))
for i in range(len(pieces)):
    print(complete_pieces[i] - pieces[i], end=" ")
