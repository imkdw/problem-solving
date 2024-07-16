from collections import Counter

s = input().upper()

c = Counter(s)
sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=True)

if len(sorted_c) == 1:
    print(sorted_c[0][0])
elif sorted_c[0][1] == sorted_c[1][1]:
    print("?")
else:
    print(sorted_c[0][0])
