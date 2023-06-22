cro_alpha = [
    "c=",
    "c-",
    "dz=",
    "d-",
    "lj",
    "nj",
    "s=",
    "z="
]
word = input()
for i in cro_alpha:
    word = word.replace(i, '*')
print(len(word))
