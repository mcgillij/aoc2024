#!/usr/bin/env python3
# day12 aoc 2024

from typing import Any
from collections import deque

Grid = list[list[str]]
Position = tuple[int, int]
Region = set[Position]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(grid: Grid, row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def find_region(
    grid: Grid,
    area: str,
    start_row: int,
    start_col: int,
) -> Region:
    queue = deque([(start_row, start_col)])
    region = set()

    while queue:
        row, col = queue.popleft()
        if not is_valid(grid, row, col):
            continue
        if grid[row][col] != area:
            continue
        if (row, col) in region:
            continue

        region.add((row, col))

        for dx, dy in DIRECTIONS:
            queue.append((row + dx, col + dy))

    return region

def find_all_regions(grid: Grid) -> list[Region]:
    seen = set()
    regions = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in seen:
                region = find_region(grid, grid[row][col], row, col)
                seen.update(region)
                regions.append(region)

    return regions

def part_1(grid: Grid) -> Any:
    regions = find_all_regions(grid)
    result = 0

    for region in regions:
        area = len(region)
        perimeter = sum(
            not is_valid(grid, row + dx, col + dy) or (row + dx, col + dy) not in region
            for row, col in region
            for dx, dy in DIRECTIONS
        )
        result += area * perimeter

    return result


def part_2(grid: Grid) -> Any:
    regions = find_all_regions(grid)
    result = 0

    for region in regions:
        area = len(region)
        seen = set()
        corners = 0

        for row, col in region:
            for dx, dy in [
                (-0.5, -0.5),
                (0.5, -0.5),
                (0.5, 0.5),
                (-0.5, 0.5),
            ]:
                new_row = row + dx
                new_col = col + dy

                if (new_row, new_col) in seen:
                    continue

                seen.add((new_row, new_col))

                adjacent = sum(
                    (new_row + r, new_col + c) in region
                    for r, c in [
                        (-0.5, -0.5),
                        (0.5, -0.5),
                        (0.5, 0.5),
                        (-0.5, 0.5),
                    ]
                )

                if adjacent == 1 or adjacent == 3:
                    corners += 1
                elif adjacent == 2:
                    # diagonal
                    pattern = [
                        (r, c) in region
                        for r, c in [
                            (new_row - 0.5, new_col - 0.5),
                            (new_row + 0.5, new_col + 0.5),
                        ]
                    ]

                    if pattern == [True, True] or pattern == [False, False]:
                        corners += 2

        result += area * corners

    return result


def read_file(filename: str) -> Grid:
    with open(filename) as f:
        grid = [list(x.strip()) for x in f.readlines()]
        return grid
# test
print(part_1(read_file("test_input")))
print(part_2(read_file("test_input")))
# real
print(part_1(read_file("day12_input")))
print(part_2(read_file("day12_input")))
