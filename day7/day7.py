#!/usr/bin/env python3
# aoc2024 day7
from itertools import product

# Evaluate expression left-to-right
def evaluate_expression(numbers, operators):
    total = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            total += numbers[i + 1]
        elif op == '*':
            total *= numbers[i + 1]
        elif op == '||':
            # Concatenate numbers
            total = int(str(total) + str(numbers[i + 1]))
    return total

# Check if any combination of operators produces the test value
def can_be_true(test_value, numbers):
    global operators
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    return any(evaluate_expression(numbers, ops) == test_value for ops in operator_combinations)

# Compute the total calibration result
def total_calibration_result(data):
    total_sum = 0
    for line in data:
        if not line.strip():  # Skip empty lines
            continue
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        if can_be_true(test_value, numbers):
            total_sum += test_value
    return total_sum

with open('day7_input') as f:
#with open('test_input') as f:
    data = f.read().strip().split('\n')
    operators = ['+', '*']
    part1 = total_calibration_result(data)
    operators = ['+', '*', '||']
    part2 = total_calibration_result(data)
    print(f"{part1=}")
    print(f"{part2=}")

