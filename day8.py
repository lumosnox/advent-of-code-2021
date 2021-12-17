
# Part 1
def calculate_part1(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            signal_pattern, output_val = line.rstrip().split(' | ')
            signal_pattern = signal_pattern.split(' ')
            output_val = output_val.split(' ')
            for val in output_val:
                if len(val) in [2, 3, 4, 7]:
                    count = count + 1
    return count


if __name__ == '__main__':
    print(calculate_part1('resources/inputs/day8/day8.txt'))

