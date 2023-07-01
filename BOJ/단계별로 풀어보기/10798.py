all_words = []
max_len = 0

for i in range(5):
    all_words.append(list(input()))



for words in all_words:
    if max_len < len(words):
        max_len = len(words)



print(max_len)
for i in range(max_len):
    for j in range(5):
        print(all_words[j][i], end="")


