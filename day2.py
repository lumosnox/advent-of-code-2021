
# Part 1
def calculate_position(filename):
    horizontal = 0
    depth = 0
    with open(filename) as file:
        for line in file:
            direction,value = line.split(' ')
            match direction:
                case 'forward':
                    horizontal = horizontal + int(value)
                case 'up':
                    depth = depth - int(value)
                case 'down':
                    depth = depth + int(value)
    return horizontal*depth


# Part 2
def calculate_position_by_instructions(filename):
    horizontal = 0
    depth = 0
    aim = 0
    with open(filename) as file:
        for line in file:
            direction, value = line.split(' ')
            match direction:
                case 'forward':
                    horizontal = horizontal + int(value)
                    depth = depth + aim*int(value)
                case 'up':
                    aim = aim - int(value)
                case 'down':
                    aim = aim + int(value)
    return horizontal * depth


if __name__ == '__main__':
    #print(calculate_position('resources/inputs/day2/day2.txt'))
    print(calculate_position_by_instructions('resources/inputs/day2/day2.txt'))

