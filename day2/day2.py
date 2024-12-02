# AoC2024 day2
    # report = [
    # [7 6 4 2 1]
    # [1 2 7 8 9]
    # [9 7 6 2 1]
    # [1 3 2 4 5]
    # [8 6 4 4 1]
    # [1 3 6 7 9]
    # ]
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

def all_ascend(report: list) -> bool:
    for i in range(1, len(report)):
        if report[i-1] > report[i]:
            return False
    return True

def all_descend(report: list) -> bool:
    for i in range(1, len(report)):
        if report[i-1] < report[i]:
            return False
    return True

def diff(report: list) -> bool:
    for i in range(1, len(report)):
        diff = abs(report[i-1] - report[i])
        if diff > 3 or diff < 1:
            return False
    return True

def is_safe(r: list) -> bool:
    if diff(r):
        if all_ascend(r) or all_descend(r):
            return True
    return False

#with open('test_input') as f:
with open('day2_input') as f:
    data = [line.strip() for line in f.readlines()]
    reports = []
    for line in data:
        l = line.split()
        l = [int(x) for x in l]
        reports.append(l)
    count = 0
    count2 = 0
    for r in reports:
        if is_safe(r):
            count += 1
            count2 += 1
        else:
            # if not is_safe(r) then remove 1 entry from the report and check again
            for i in range(0, len(r)):
                new_r = r.copy()
                new_r.pop(i)
                if is_safe(new_r):
                    count2 += 1
                    break


    # part1
    print(f"Part1: {count}")
    # part2
    print(f"Part2: {count2}")
