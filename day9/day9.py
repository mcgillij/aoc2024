#!/usr/bin/env python3
# aoc2024 day9

def part1(data: str) -> int:
    file_length, free_space, p = [], [], 0
    for i, c in enumerate(data):
        [file_length, free_space][i % 2] += [[*range(p, p := p + int(c))]]

    free_space = sum(free_space, [])
    for f in reversed(file_length):
        for x in reversed(range(len(f))):
            if len(free_space) and f[x] > free_space[0]:
                f[x] = free_space.pop(0)

    return(sum(i * j for i, f in enumerate(file_length) for j in f))

def part2(data: str) -> int:
    file_length, free_space, p = [], [], 0
    for i, c in enumerate(data):
        [file_length, free_space][i % 2] += [[*range(p, p := p + int(c))]]

    for y in reversed(range(len(file_length))):
        for x in range(len(free_space)):
            if len(free_space[x]) >= len(file_length[y]) and file_length[y][0] > free_space[x][0]:
                file_length[y] = free_space[x][:len(file_length[y])]
                free_space[x] = free_space[x][len(file_length[y]):]

    return(sum(i * j for i, f in enumerate(file_length) for j in f))

if __name__ == "__main__":
    data = open('day9_input').read().strip()
    print(f"Part1: {part1(data)}")
    print(f"Part2: {part2(data)}")

