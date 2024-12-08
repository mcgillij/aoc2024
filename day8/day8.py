#!/usr/bin/env python3
# aoc2024 day8

from collections import defaultdict

def build_antenna_map(data):
    _map = [list(line) for line in data]
    antennas = defaultdict(list)
    rows, cols = len(_map), len(_map[0])

    for row in range(rows):
        for col in range(cols):
            if _map[row][col] != ".":
                antennas[_map[row][col]].append((row, col))

    return antennas, rows, cols

def find_antinodes(antennas, rows, cols, part2=False):
    antinodes = set()

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                for _idx, _dir in [(i, -1), (j, 1)]:
                    if part2:
                        pos = coords[_idx]
                        while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)
                            pos = tuple([a + b * _dir for a, b in zip(pos, diff)])
                    else:
                        pos = tuple([a + b * _dir for a, b in zip(coords[_idx], diff)])
                        if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)

    return antinodes

def part1(data):
    antennas, rows, cols = build_antenna_map(data)
    antinodes = find_antinodes(antennas, rows, cols)
    return len(antinodes)

def part2(data):
    antennas, rows, cols = build_antenna_map(data)
    antinodes = find_antinodes(antennas, rows, cols, part2=True)
    return len(antinodes)

data = [line.strip() for line in open("test_input") if line.strip()]
#data = [line.strip() for line in open("day8_input") if line.strip()]
print(part1(data))
print(part2(data))
