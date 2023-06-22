credit = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

scores = []
jungong = 0
hakjum = 0
for i in range(20):
    class_info = input()
    scores.append(class_info)

for i in range(len(scores)):
    split_arr = scores[i].split(' ')
    if (split_arr[2] == 'P'):
        continue
    jungong += float(split_arr[1]) * credit[split_arr[2]]
    hakjum += float(split_arr[1])

print(jungong / hakjum)