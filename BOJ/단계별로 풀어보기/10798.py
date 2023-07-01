all_words = [list(input()) for i in range(5)]
max_len = max(len(i) for i in all_words)
with_space_words = [arr + [''] * (max_len - len(arr)) for arr in all_words]
for i in range(max_len):
    for j in range(5):
        print(with_space_words[j][i], end="")
