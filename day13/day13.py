#!/usr/bin/env python3
# day13 aoc 2024

from typing import NamedTuple, Optional, List, Tuple
from fractions import Fraction

class ClawMachine(NamedTuple):
    button_a: Tuple[int, int]  # (X, Y) movement for button A
    button_b: Tuple[int, int]  # (X, Y) movement for button B
    prize: Tuple[int, int]     # (X, Y) position of prize

def parse_input(text: str) -> List[ClawMachine]:
    """Parse the input text into a list of ClawMachine objects."""
    machines = []
    current_a = current_b = current_prize = None

    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('Button A:'):
            parts = line.split(',')
            x = int(parts[0].split('+')[1])
            y = int(parts[1].split('+')[1])
            current_a = (x, y)
        elif line.startswith('Button B:'):
            parts = line.split(',')
            x = int(parts[0].split('+')[1])
            y = int(parts[1].split('+')[1])
            current_b = (x, y)
        elif line.startswith('Prize:'):
            parts = line.split(',')
            x = int(parts[0].split('=')[1])
            y = int(parts[1].split('=')[1])
            current_prize = (x, y)

            if all(v is not None for v in [current_a, current_b, current_prize]):
                machines.append(ClawMachine(current_a, current_b, current_prize))
                current_a = current_b = current_prize = None

    return machines

def parse_number(line: str, index: int) -> Tuple[int, int]:
    '''Parse the number starting at line[index] and the first index after
       it.'''
    acc = ''
    while index < len(line) and line[index].isdigit():
        acc += line[index]
        index += 1

    return int(acc), index

def parse_coords(line: str) -> Tuple[int, int]:
    '''Parse the X and Y coordinates of a button or prize.'''

    # find X then skip past 1 character
    index = line.find('X') + 2

    # parse the X value then skip 4 characters
    x, index = parse_number(line, index)
    index += 4

    # parse Y and return
    y, _ = parse_number(line, index)

    return x, y

def parse_machine(src: str) -> ClawMachine:
    '''Parse the button and prize coordinates of a machine.'''
    lines = src.strip().split('\n')
    button_a_line = next(line for line in lines if 'Button A' in line)
    button_b_line = next(line for line in lines if 'Button B' in line)
    prize_line = next(line for line in lines if 'Prize' in line)

    button_a = parse_coords(button_a_line)
    button_b = parse_coords(button_b_line)
    prize = parse_coords(prize_line)

    return ClawMachine(button_a, button_b, prize)

def solve(a1: int, a2: int, b1: int, b2: int, c1: int, c2: int) -> Tuple[Optional[Fraction], Optional[Fraction]]:
    '''Solve a two-variable system of linear equations.'''

    # use special case of Cramer's rule:
    denom = a1 * b2 - a2 * b1
    if denom == 0:
        return None, None

    # No floating-point inaccuracy issues with Fraction!
    x = Fraction(b2 * c1 - b1 * c2, denom)
    y = Fraction(a1 * c2 - c1 * a2, denom)
    return x, y

def is_integer(n: Fraction) -> bool:
    return n.denominator == 1

def in_range(n: Optional[Fraction]) -> bool:
    '''Check if n is a valid number of presses'''
    return n is not None and is_integer(n) and n >= 0

def cost(a, b, prize) -> int:
    '''Calculate the token cost of winning the prize for this machine.

       A machine with no solution has a 'cost' of 0.'''
    #prize = (prize[0], prize[1]) # part 1
    prize = (prize[0] + 10000000000000, prize[1] + 10000000000000) # part 2
    a_presses, b_presses = solve(*a, *b, *prize)
    if in_range(a_presses) and in_range(b_presses):
        return 3 * a_presses + b_presses
    else:
        return 0

def main(machines: List[ClawMachine]) -> int:
    '''Calculate the total cost of winning each possible machine.'''
    return sum(cost(machine.button_a, machine.button_b, machine.prize) for machine in machines)

if __name__ == '__main__':
    with open("day13_input") as f:
    #with open("test_input") as f:
        input_text = f.read()
        machines = parse_input(input_text)
        print(main(machines))

