import string

s = input()

alapa = string.ascii_lowercase

for a in alapa:
    if a in s:
        print(s.index(a))
    else:
        print(-1)

