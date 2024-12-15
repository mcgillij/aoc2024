import re
from dataclasses import dataclass
from typing import List, Dict, Tuple
from collections import defaultdict
import time

@dataclass
class Robot:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int

def parse_input(input_text: str) -> List[Robot]:
    robots = []
    for line in input_text.strip().split('\n'):
        numbers = [int(n) for n in re.findall(r'-?\d+', line)]
        robots.append(Robot(numbers[0], numbers[1], numbers[2], numbers[3]))
    return robots

def print_grid(positions: Dict[Tuple[int, int], int], width: int, height: int, step: int):
    print(f"\nTime step: {step}")
    print("-" * width)
    for y in range(height):
        row = ""
        for x in range(width):
            count = positions.get((x, y), 0)
            if count == 0:
                row += " "
            elif count < 10:
                row += str(count)
            else:
                row += "#"  # For counts >= 10
        print(row)
    print("-" * width)

def simulate_with_visualization(robots: List[Robot], width: int, height: int, seconds: int, 
                              print_interval: int = 1, max_steps: int = None) -> Dict[Tuple[int, int], int]:
    if max_steps is None:
        max_steps = seconds
        
    current_positions = defaultdict(int)
    
    # Initialize starting positions
    for robot in robots:
        current_positions[(robot.pos_x, robot.pos_y)] += 1
    
    # Print initial state
    print_grid(current_positions, width, height, 0)
    
    # Simulate each step
    for step in range(1, max_steps + 1):
        current_positions = defaultdict(int)
        
        for robot in robots:
            # Calculate position at this step
            total_x = robot.pos_x + (robot.vel_x * step)
            total_y = robot.pos_y + (robot.vel_y * step)
            
            # Apply wrapping
            final_x = total_x % width
            final_y = total_y % height
            
            # Add to position map
            current_positions[(final_x, final_y)] += 1
        
        # Print grid at specified intervals
        if step % print_interval == 0:
            print_grid(current_positions, width, height, step)
            time.sleep(0.2)  # Add small delay to make visualization easier to follow
    
    # If we're not simulating all steps, calculate final position
    if max_steps < seconds:
        final_positions = defaultdict(int)
        for robot in robots:
            total_x = robot.pos_x + (robot.vel_x * seconds)
            total_y = robot.pos_y + (robot.vel_y * seconds)
            final_x = total_x % width
            final_y = total_y % height
            final_positions[(final_x, final_y)] += 1
        return final_positions
    
    return current_positions

def calculate_safety_factor(position_map: Dict[Tuple[int, int], int], width: int, height: int) -> int:
    quadrants = [0, 0, 0, 0]
    mid_x = width // 2
    mid_y = height // 2
    
    for (x, y), count in position_map.items():
        if x == mid_x or y == mid_y:
            continue
        quadrant_idx = (int(x > mid_x) << 1) | int(y > mid_y)
        quadrants[quadrant_idx] += count
    
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    
    return safety_factor

def solve_puzzle(input_text: str, width: int = 101, height: int = 103, seconds: int = 100, 
                visualize: bool = False, print_interval: int = 1, max_steps: int = None) -> int:
    robots = parse_input(input_text)
    
    if visualize:
        position_map = simulate_with_visualization(robots, width, height, seconds, 
                                                print_interval, max_steps)
    else:
        position_map = simulate_with_visualization(robots, width, height, seconds, 
                                                max_steps=0)  # Only calculate final position
    
    return calculate_safety_factor(position_map, width, height)


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read().strip()

# Test with visualization
# To see first 10 steps with updates every 2 steps:
result = solve_puzzle(read_file("day14_input"), width=101, height=103, seconds=10000, 
#result = solve_puzzle(read_file("test_input"), width=11, height=7, seconds=100, 
                     visualize=True, print_interval=1, max_steps=10000)
print(f"\nFinal safety factor: {result}")

# To solve actual puzzle without visualization:
# result = solve_puzzle(puzzle_input)
