input_pieces = list(map(int, input().split()))
all_pieces = [1, 1, 2, 2, 2, 8]
for index in range(len(input_pieces)):
    print(all_pieces[index] - input_pieces[index], end=' ')