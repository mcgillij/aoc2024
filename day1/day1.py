# AoC2024 day1

def difference(a: int, b: int) -> int:
    # difference between two items subtracting the smallest from the largest
    if a > b:
        return a - b
    else:
        return b - a


def count_occurrences(number: int, array: list) -> int:
    # number of occurrences of the number in the list
    count = 0
    for i in array:
        if i == number:
            count += 1
    return count


def compute_new_list(array_1: list, array_2: list) -> list:
    # compute new list based on count_occurrences
    new_list = []
    for i in range(len(array_1)):
        new_num = count_occurrences(array_1[i], array_2)
        new_list.append(array_1[i] * new_num)  # similarity score
    return new_list


#with open('test_input') as f:
with open('day1_input') as f:
    data = [line.strip() for line in f.readlines()]
    a_list = []
    b_list = []
    for line in data:
        a, b = line.split()
        a_list.append(int(a))
        b_list.append(int(b))
    sorted_a = sorted(a_list)
    sorted_b = sorted(b_list)

    new_a = compute_new_list(a_list, sorted_b)
    new_b = compute_new_list(b_list, sorted_a)
    new_sorted_a = sorted(new_a)
    results = []
    for i in range(len(new_sorted_a)):
        results.append(difference(sorted_a[i], sorted_b[i]))
    # part1
    print(f"Part1: {sum(results)}")
    # part2
    print(f"Part2: {sum(new_a)}")
