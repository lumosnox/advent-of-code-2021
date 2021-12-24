
# Part 1
def calculate_part1(filename):
    paper = []
    points = []
    max_x = 0
    max_y = 0
    fold1 = ''
    with open(filename) as file:
        for line in file:
            if line != '\n':
                x, y = (int(x) for x in line.rstrip().split(','))
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
                points.append((x, y))
            else:
                fold1 = file.readline().rstrip()
                break

    for col in range(0, max_y+1):
        row = [0] * (max_x+1)
        paper.append(row)

    for (x, y) in points:
        paper[y][x] = 1

    if 'x' in fold1:
        _, x = fold1.split('=')
        fold_left(paper, int(x), max_x, max_y)

    if 'y' in fold1:
        _, y = fold1.split('=')
        fold_up(paper, int(y), max_x, max_y)

    visible_dots = calculate_visible_dots(paper, max_x, max_y)

    return visible_dots


def calculate_visible_dots(grid, max_x, max_y):
    visible_dots = 0
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            visible_dots = visible_dots + grid[y][x]
    return visible_dots


def fold_left(paper, x, max_x, max_y):
    x = x +1
    for x_coord in range(0, x):
        for y_coord in range(0, max_y+1):
            if paper[y_coord][max_x-x_coord] == 1:
                paper[y_coord][x_coord] = 1
                paper[y_coord][max_x - x_coord] = 0
    for y_coord in range(0, max_y + 1):
        paper[y_coord][x] = 0


def fold_up(paper, y, max_x, max_y):
    y = y + 1
    for x_coord in range(0, max_x+1):
        for y_coord in range(0, y):
            if paper[max_y - y_coord][x_coord] == 1:
                paper[y_coord][x_coord] = 1
                paper[max_y - y_coord][x_coord] = 0
        paper[y][x_coord] = 0


# Part 2
# there must be a bug - part 2 is not correct!
def calculate_part2(filename):
    paper = []
    points = []
    max_x = 0
    max_y = 0
    folds = []
    with open(filename) as file:
        for line in file:
            if line != '\n':
                x, y = (int(x) for x in line.rstrip().split(','))
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
                points.append((x, y))
            else:
                for i in range(0, 12):
                    line = file.readline().rstrip()
                    folds.append(line)
                break

    for col in range(0, max_y+1):
        row = [0] * (max_x+1)
        paper.append(row)

    for (x, y) in points:
        paper[y][x] = 1

    for fold in folds:
        if 'x' in fold:
            _, x = fold.split('=')
            fold_left(paper, int(x), max_x, max_y)

        if 'y' in fold:
            _, y = fold.split('=')
            fold_up(paper, int(y), max_x, max_y)

    visible_dots = calculate_visible_dots(paper, max_x, max_y)

    return visible_dots


if __name__ == '__main__':
    print(calculate_part1('resources/inputs/day13/day13.txt'))
    #print(calculate_part2('resources/inputs/day13/day13.txt'))

