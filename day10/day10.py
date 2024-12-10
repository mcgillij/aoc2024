#!/usr/bin/env python3
# aoc2024 day10
from collections import deque

def parse_map(file_path):
    with open(file_path) as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads(grid):
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def bfs_for_score(grid, start):
    queue = deque([start])
    visited = set()
    score = 0
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if grid[r][c] == 9:
            score += 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c] + 1:
                queue.append((nr, nc))
    return score

def sum_of_trailhead_scores(file_path) -> int:
    grid = parse_map(file_path)
    trailheads = find_trailheads(grid)
    total_score = sum(bfs_for_score(grid, trailhead) for trailhead in trailheads)
    return total_score

def count_trails_to_peak(grid, r, c, prev_value):
    """
    Count trails that reach a peak (value 9) from current position.
    Only moves to adjacent positions with value = prev_value + 1.
    """
    current_value = grid[r][c]
    if current_value != prev_value + 1:
        return 0
    if current_value == 9:  # Reached a peak
        return 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    total_trails = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            total_trails += count_trails_to_peak(grid, nr, nc, current_value)
    return total_trails

def sum_of_trailhead_ratings(file_path) -> int:
    """Calculate the sum of all trailhead ratings in the map."""
    grid = parse_map(file_path)
    trailheads = find_trailheads(grid)
    total = 0
    for i, (r, c) in enumerate(trailheads, 1):
        # Count trails starting from each trailhead
        rating = count_trails_to_peak(grid, r, c, -1)  # Start with prev_value = -1 since we're at 0
        #print(f"Trailhead {i} at ({r}, {c}): Rating = {rating}")
        total += rating
    return total

if __name__ == "__main__":
    part1 = sum_of_trailhead_scores("day10_input")
    part2 = sum_of_trailhead_ratings("day10_input")
    # part1 = sum_of_trailhead_scores("test_input")
    # part2 = sum_of_trailhead_ratings("test_input")
    print(f"{part1=}")
    print(f"{part2=}")
