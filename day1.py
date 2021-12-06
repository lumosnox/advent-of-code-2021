
# Part 1
def calculate_depth_increase(filename):
    previous = -1
    count = -1  # offset the first input
    with open(filename) as file:
        for line in file:
            if int(line.rstrip()) > previous:
                count = count + 1
            previous = int(line.rstrip())
    return count


# Part 2
def calculate_sum_increase(filename):
    input_list = []
    prev_sum = -1
    count = -1  # offset the first input
    window_size = 3  # A starts at 0, E starts at 4, ...

    #  read file and save the input
    with open(filename) as file:
        for line in file:
            input_list.append(int(line.rstrip()))

    l = len(input_list)
    for i in range(0, l):
        if (i + (window_size - 1)) <= (l-1):
            sum = input_list[i] + input_list[i+1] + input_list[i+2]
            if sum > prev_sum:
                count = count + 1
            prev_sum = sum
        else:
            break

    return count


if __name__ == '__main__':
    #print(calculate_depth_increase('resources/inputs/day1.txt'))
    print(calculate_sum_increase('resources/inputs/day1.txt'))