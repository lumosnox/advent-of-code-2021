# Part 1
def calculate_part1(filename):
    grid = {}
    with open(filename) as file:
        for line in file:
            coord1, coord2 = line.split(' -> ')
            x1, y1 = [int(c) for c in coord1.split(',')]
            x2, y2 = [int(c) for c in coord2.split(',')]
            update_grid(x1, y1, x2, y2, grid)

    return calculate_overlapping(grid)


def update_grid(x1, y1, x2, y2, grid):
    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2+1):
                mark_coord(x1, y, grid)
        else:
            for y in range(y2, y1+1):
                mark_coord(x1, y, grid)
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2+1):
                mark_coord(x, y1, grid)
        else:
            for x in range(x2, x1+1):
                mark_coord(x, y1, grid)
    else:
        pass  # todo


def mark_coord(x, y, grid):
    if (x, y) in grid:
        grid[(x, y)] = grid[(x, y)] + 1
    else:
        grid[(x, y)] = 1


def calculate_overlapping(grid):
    overlapping = 0
    for coord_set, count in grid.items():
        if count > 1:
            overlapping = overlapping + 1
    return overlapping


##############################################
# Part 2
def calculate_part2(filename):
    grid = {}
    with open(filename) as file:
        for line in file:
            coord1, coord2 = line.split(' -> ')
            x1, y1 = [int(c) for c in coord1.split(',')]
            x2, y2 = [int(c) for c in coord2.split(',')]
            update_grid2(x1, y1, x2, y2, grid)

    return calculate_overlapping(grid)


def update_grid2(x1, y1, x2, y2, grid):
    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2+1):
                mark_coord(x1, y, grid)
        else:
            for y in range(y2, y1+1):
                mark_coord(x1, y, grid)
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2+1):
                mark_coord(x, y1, grid)
        else:
            for x in range(x2, x1+1):
                mark_coord(x, y1, grid)
    else:
        if x1 < x2:
            # start from (x1, y1)
            if y1 < y2:
                for x in range(x1, x2 + 1):
                    mark_coord(x, y1, grid)
                    y1 = y1 + 1
            else:
                for x in range(x1, x2 + 1):
                    mark_coord(x, y1, grid)
                    y1 = y1 - 1
        else:
            # start from (x2, y2)
            if y1 < y2:
                for x in range(x2, x1 + 1):
                    mark_coord(x, y2, grid)
                    y2 = y2 - 1
            else:
                for x in range(x2, x1 + 1):
                    mark_coord(x, y2, grid)
                    y2 = y2 + 1


if __name__ == '__main__':
    #print(calculate_part1('resources/inputs/day5/day5.txt'))
    print(calculate_part2('resources/inputs/day5/day5.txt'))

