person, area = map(int, input().split())
guess_person = map(int, input().split())
all_person = person * area
for i in guess_person:
    print(i - all_person, end=' ')