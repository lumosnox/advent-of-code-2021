
# Part 1
def calculate_part1(filename):
    risk_level = 0
    matrix = []
    # format input
    with open(filename) as file:
        level = 0
        for line in file:
            matrix.append([])
            for c in line.rstrip():
                matrix[level].append(int(c))
            level = level + 1

    # analyze input
    cols = len(matrix[0])
    rows = len(matrix)
    for i in range(0, rows):
        for j in range(0, cols):
            point = matrix[i][j]
            up = 10
            down = 10
            left = 10
            right = 10
            if j-1 > -1:
                left = matrix[i][j-1]
            if j+1 < cols:
                right = matrix[i][j+1]
            if i+1 < rows:
                down = matrix[i+1][j]
            if i-1 > -1:
                up = matrix[i-1][j]
            if point < left and point < right and point < up and point < down:
                risk_level = risk_level + point + 1
    return risk_level


if __name__ == '__main__':
    print(calculate_part1('resources/inputs/day9/day9.txt'))

