# AoC2024 day3

import re

def sum_of_multiplications(corrupted_memory):
    # Regular expression pattern to match valid 'mul' instructions
    pattern = r'mul\s*\((\d{1,3}),\s*(\d{1,3})\)'
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    total_sum = 0
    # Iterate over each match and calculate the product
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    return total_sum

def sum_of_enabled_multiplications(corrupted_memory):
    # Regular expression pattern to match valid 'mul' instructions
    mul_pattern = r'mul\s*\((\d{1,3}),\s*(\d{1,3})\)'
    # Pattern to match 'do()' and 'don't()'
    do_pattern = r'do\s*\(\s*\)'
    dont_pattern = r"don't\s*\(\s*\)"
    # Find all matches in the corrupted memory
    mul_matches = re.finditer(mul_pattern, corrupted_memory)
    do_matches = re.finditer(do_pattern, corrupted_memory)
    dont_matches = re.finditer(dont_pattern, corrupted_memory)
    total_sum = 0
    enable_mul = True
    # List to store all events (mul, do, don't) along with their positions
    events = []
    for match in mul_matches:
        events.append(('mul', match.start(), match.groups()))
    for match in do_matches:
        events.append(('do', match.start(), None))
    for match in dont_matches:
        events.append(("don't", match.start(), None))
    # Sort events by their positions
    events.sort(key=lambda x: x[1])
    for event_type, _, data in events:
        if event_type == 'mul':
            if enable_mul:
                x, y = map(int, data)
                total_sum += x * y
        elif event_type == 'do':
            enable_mul = True
        elif event_type == "don't":
            enable_mul = False
    return total_sum


#with open('test_input') as f:
with open('day3_input') as f:
    data = f.read()
    part1 = sum_of_multiplications(data)
    part2 = sum_of_enabled_multiplications(data)
    print(f"Part1: {part1}")
    print(f"Part2: {part2}")
