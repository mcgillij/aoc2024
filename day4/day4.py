# AoC2024 day4
def count_orientations(grid, word):
    def is_valid(i, j, di, dj, word_length):
        # Check if the current orientation is within bounds and matches the word
        return all(
            0 <= i + k * di < len(grid) and
            0 <= j + k * dj < len(grid[i]) and
            grid[i + k * di][j + k * dj] == word[k]
            for k in range(word_length)
        )

    count = 0
    n, m = len(grid), len(grid[0])
    word_length = len(word)

    # Check all possible starting positions and orientations
    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                # Horizontal forward
                if is_valid(i, j, 0, 1, word_length): count += 1
                # Horizontal backward
                if is_valid(i, j, 0, -1, word_length): count += 1
                # Vertical forward
                if is_valid(i, j, 1, 0, word_length): count += 1
                # Vertical backward
                if is_valid(i, j, -1, 0, word_length): count += 1
                # Diagonal forward (down-right)
                if is_valid(i, j, 1, 1, word_length): count += 1
                # Diagonal backward (up-left)
                if is_valid(i, j, -1, -1, word_length): count += 1
                # Diagonal forward (up-right)
                if is_valid(i, j, -1, 1, word_length): count += 1
                # Diagonal backward (down-left)
                if is_valid(i, j, 1, -1, word_length): count += 1

    return count

def count_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_mas(word):
        return word in ("MAS", "SAM")

    # Iterate over the grid to check for X-MAS patterns
    for r in range(rows - 2):  # Ensure space for the 3-row X
        for c in range(cols - 2):  # Ensure space for the 3-column X
            # Extract the X pattern
            top = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]  # Top-left to bottom-right
            bottom = grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]  # Bottom-left to top-right

            # Check if both diagonals are MAS or SAM
            if is_mas(top) and is_mas(bottom):
                count += 1

    return count

#with open('test_input') as f:
with open('day4_input') as f:
    data = [line.strip() for line in f.readlines()]
    part1 = count_orientations(data, 'XMAS')
    part2 = count_x_mas_patterns(data)
    print(f"{part1=}")  # Output should be the number of times 'XMAS' appears
    print(f"{part2=}")  # Output should be the number of times 'XMAS' appears
