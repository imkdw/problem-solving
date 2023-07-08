P, N = map(int, input().split())
person_count = list(map(int, input().split()))
for person in person_count:
    print(person - P * N, end=" ")