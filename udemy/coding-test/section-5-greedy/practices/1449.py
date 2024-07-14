# https://www.acmicpc.net/problem/1449

def exhaustive_search():
    leak_count, tape_length = map(int, input().split())

    leak_pos = map(int, input().split())
    coords = [False] * 1001
    for pos in leak_pos:
        coords[pos] = True

    used_tape_count = 0
    i = 0
    while i < 1001:
        if coords[i]:
            used_tape_count += 1
            i += tape_length
        else:
            i += 1

    print(used_tape_count)

def greedy():
    leak_count, tape_length = map(int, input().split())
    leak_pos = sorted(map(int, input().split()))

    used_tape_count = 0
    tape_end = 0

    for pos in leak_pos:
        if pos > tape_end:
            used_tape_count += 1
            tape_end = pos + tape_length - 1

    print(used_tape_count)


greedy()