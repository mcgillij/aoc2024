#!/usr/bin/env python3
# day11 aoc 2024
from collections import defaultdict

#with open("test_input") as f:
with open("day11_input") as f:
    nums = list(map(int, f.read().split()))
    my_dict = defaultdict(int)
    # populate the dictionary with the numbers from our input
    for num in nums: my_dict[num] += 1
    part1_blinks = 25
    part2_blinks = 75
    for i in range(part2_blinks): 
        if i == part1_blinks:
            print(sum(my_dict.values()))
        updates = defaultdict(int)

        for k, v in my_dict.items():
            s = str(k)
            updates[k] -= v

            if k == 0: 
                updates[1] += v
            elif len(s) % 2 == 0:
                l, r = s[:len(s)//2], s[len(s)//2:]
                updates[int(l)] += v
                updates[int(r)] += v
            else: 
                updates[k*2024] += v

        for k, v in updates.items():
            my_dict[k] += v
            if my_dict[k] == 0: my_dict.pop(k)

    print(sum(my_dict.values()))

