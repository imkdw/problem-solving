name, age, weight = input().split()
if name != '#' and (int(age) > 17 or int(weight) >= 80):
    print(name, 'Junior')
else:
    print(name, 'Senior')