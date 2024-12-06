def is_loop_detected(visited_positions, current_position, direction):
    return (current_position, direction) in visited_positions

def count_visited_positions_with_obstruction(grid, start_row, start_col, obstruction_row, obstruction_col):
    n, m = len(grid), len(grid[0])
    # Place the obstruction
    grid[obstruction_row][obstruction_col] = '#'

    # Movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 3  # Start facing up
    visited_positions = set()
    row, col = start_row, start_col

    while True:
        visited_positions.add(((row, col), directions[direction_index]))
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        # End simulation if moving out of bounds
        if not (0 <= next_row < n and 0 <= next_col < m):
            grid[obstruction_row][obstruction_col] = '.'  # Restore grid
            return False

        if grid[next_row][next_col] == '#':
            # Turn 90 degrees clockwise at an obstacle
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
            # Check for loop
            if is_loop_detected(visited_positions, (row, col), directions[direction_index]):
                grid[obstruction_row][obstruction_col] = '.'  # Restore grid
                return True


def find_all_valid_obstruction_positions(puzzle_input):
    lines = puzzle_input.strip().split('\n')
    grid = [list(line) for line in lines]
    n, m = len(grid), len(grid[0])
    # Find starting position
    start_row, start_col = next((r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == '^')
    valid_positions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and (i, j) != (start_row, start_col):
                if count_visited_positions_with_obstruction(grid, start_row, start_col, i, j):
                    valid_positions.append((i, j))
    return len(valid_positions)


def count_visited_positions(puzzle_input):
    lines = puzzle_input.strip().split('\n')
    grid = [list(line) for line in lines]
    n, m = len(grid), len(grid[0])

    # Find starting position and direction
    start_row, start_col = 0, 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                start_row, start_col = i, j
                break

    # Movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 3  # Start moving up
    visited_positions = set()
    row, col = start_row, start_col

    while True:
        # Add current position to visited
        visited_positions.add((row, col))
        # Try moving forward
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
        # End simulation if moving out of bounds
        if not (0 <= next_row < n and 0 <= next_col < m):
            break
        if grid[next_row][next_col] == '#':
            # Turn 90 degrees clockwise at an obstacle
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
    return len(visited_positions)


#with open('test_input') as f:
with open('day6_input') as f:
    data = f.read()
    print(f"Part1: {count_visited_positions(data)}")
    print(f"Part2: {find_all_valid_obstruction_positions(data)}")
