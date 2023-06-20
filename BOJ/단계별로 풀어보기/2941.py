cro_alpha = {
    1: "c=",
    2: "c-",
    3: "dz=",
    4: "d-",
    5: "lj",
    6: "nj",
    7: "s=",
    8: "z="
}
cnt = 0
word = input()
for alpha in cro_alpha:
    if cro_alpha[alpha] in word:
        print(cro_alpha[alpha])
        cnt += 1

print(cnt)