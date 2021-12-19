
# Part 1
def calculate_part1(filename, steps):
    flashes = 0
    matrix = []
    with open(filename) as file:
        row = -1
        for line in file:
            row = row + 1
            matrix.append([])
            for c in line.rstrip():
                matrix[row].append(int(c))

    rows = len(matrix)
    columns = len(matrix[0])
    for step in range(0, steps):
        flashes_to_perform = []
        # increase energy levels by 1
        for r in range(0, rows):
            for c in range(0, columns):
                matrix[r][c] = (matrix[r][c] + 1) % 10
                if matrix[r][c] == 0:
                    flashes = flashes + 1
                    flashes_to_perform.append((r, c))
        # perform flashes that were triggered by another flash that step
        for (row, col) in flashes_to_perform:
            flashes = flashes + perform_flash(matrix, row, col)

    return flashes


def perform_flash(matrix, r, c):
    flashes = 0
    rows = len(matrix)
    columns = len(matrix[0])
    flashes_to_perform = []

    adjacent_octopuses = []
    if 0 <= c - 1 < columns:
        adjacent_octopuses.append((r, c-1))

    if 0 <= c + 1 < columns:
        adjacent_octopuses.append((r, c+1))

    if 0 <= r - 1 < rows:
        adjacent_octopuses.append((r-1, c))
        if 0 <= c - 1 < columns:
            adjacent_octopuses.append((r-1, c-1))
        if 0 <= c + 1 < columns:
            adjacent_octopuses.append((r-1, c+1))

    if 0 <= r + 1 < rows:
        adjacent_octopuses.append((r+1, c))
        if 0 <= c - 1 < columns:
            adjacent_octopuses.append((r+1, c-1))
        if 0 <= c + 1 < columns:
            adjacent_octopuses.append((r+1, c+1))

    # increase energy levels of adjacent octopuses
    for (r, c) in adjacent_octopuses:
        if matrix[r][c] != 0:
            matrix[r][c] = (matrix[r][c] + 1) % 10
            if matrix[r][c] == 0:
                flashes = flashes + 1
                flashes_to_perform.append((r, c))

    # perform flashes that were triggered by another flash that step
    for (row, col) in flashes_to_perform:
        flashes = flashes + perform_flash(matrix, row, col)

    return flashes


# Part 2
def calculate_part2(filename, steps):
    matrix = []
    with open(filename) as file:
        row = -1
        for line in file:
            row = row + 1
            matrix.append([])
            for c in line.rstrip():
                matrix[row].append(int(c))

    rows = len(matrix)
    columns = len(matrix[0])
    num_octopuses = rows * columns
    for step in range(0, steps):
        flashes_per_step = 0
        flashes_to_perform = []
        # increase energy levels by 1
        for r in range(0, rows):
            for c in range(0, columns):
                matrix[r][c] = (matrix[r][c] + 1) % 10
                if matrix[r][c] == 0:
                    flashes_per_step = flashes_per_step + 1
                    flashes_to_perform.append((r, c))
        # perform flashes that were triggered by another flash that step
        for (row, col) in flashes_to_perform:
            flashes_per_step = flashes_per_step + perform_flash(matrix, row, col)
        if num_octopuses == flashes_per_step:
            return step + 1
    return -1


if __name__ == '__main__':
    print(calculate_part2('resources/inputs/day11/day11.txt', 1000))

