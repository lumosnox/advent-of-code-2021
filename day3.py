
# Part 1
# note: we are not currently using the binary versions of the gamma/epsilon rates in the implementation below
# (in the initial implementation idea the decimal numbers would be calculated from them, but they can be also
# calculated along-side - as below - though slightly less obvious, this is more efficient)
# notes: possible enhancement - calculate the number size from the file rather than giving it as an input
def calculate_power_consumption(filename, number_size):
    gamma_rate_binary = []
    gamma_rate = 0
    epsilon_rate_binary = []  # this is the mirror of gamma rate, actually
    epsilon_rate = 0
    num_of_lines = 0
    # initialize
    zero_bits_num = []
    for i in range(0, number_size):
        zero_bits_num.append(0)

    # read input
    with open(filename) as file:
        for line in file:
            num_of_lines = num_of_lines + 1
            for i in range(0, number_size):
                if line[i] == '0':
                    zero_bits_num[i] = zero_bits_num[i] + 1

    # do post-processing
    midpoint = num_of_lines // 2 + num_of_lines % 2  # find the majority we need to check for most common bit
    for i in range(0, number_size):
        if zero_bits_num[i] >= midpoint:
            gamma_rate_binary.append(0)
            epsilon_rate_binary.append(1)
            epsilon_rate = epsilon_rate + pow(2, (number_size-1-i))
        else:
            gamma_rate_binary.append(1)
            gamma_rate = gamma_rate + pow(2, (number_size-1-i))
            epsilon_rate_binary.append(0)

    return gamma_rate * epsilon_rate


# Part 2
def calculate_life_support_rating(filename, number_size):
    input_lines = []
    num_of_lines = 0

    # initialize
    zero_bits_num = []
    for i in range(0, number_size):
        zero_bits_num.append(0)

    # read input
    with open(filename) as file:
        for line in file:
            input_lines.append(line.rstrip('\n'))
            num_of_lines = num_of_lines + 1
            if line[0] == '0':
                zero_bits_num[0] = zero_bits_num[0] + 1

    # do post-processing
    oxygen_generator_rating_candidates = input_lines
    scrubber_rating_candidates = input_lines

    for i in range(0, number_size):
        most_common_bit = calculate_bit(oxygen_generator_rating_candidates, i, True)
        oxygen_generator_rating_candidates = filter_by_index_val(i, most_common_bit, oxygen_generator_rating_candidates)
        if len(oxygen_generator_rating_candidates) == 1:
            break
    for i in range(0, number_size):
        least_common_bit = calculate_bit(scrubber_rating_candidates, i, False)
        scrubber_rating_candidates = filter_by_index_val(i, least_common_bit, scrubber_rating_candidates)
        if len(scrubber_rating_candidates) == 1:
            break

    oxygen_generator_rating_binary = oxygen_generator_rating_candidates[0]
    scrubber_rating_binary = scrubber_rating_candidates[0]

    oxygen_generator_rating = convert_to_decimal(oxygen_generator_rating_binary)
    scrubber_rating = convert_to_decimal(scrubber_rating_binary)

    return oxygen_generator_rating * scrubber_rating


def convert_to_decimal(binary_num):
    l = len(binary_num)
    decimal_val = 0
    for i in range(0, l):
        decimal_val = decimal_val + int(binary_num[i])*pow(2, (l - 1 - i))
    return decimal_val


def calculate_bit(values, index, ox_rt_flag):
    num_of_values = 0
    zero_bits_num = 0
    for value in values:
        num_of_values = num_of_values + 1
        if value[index] == '0':
            zero_bits_num = zero_bits_num + 1
    midpoint = num_of_values / 2
    if zero_bits_num > midpoint:
        if ox_rt_flag:
            return "0"
        else:
            return "1"
    elif zero_bits_num == midpoint:
        if ox_rt_flag:
            return "1"
        else:
            return "0"
    else:
        if ox_rt_flag:
            return "1"
        else:
            return "0"


def filter_by_index_val(index, value, input_list):
    filtered = []
    for el in input_list:
        if el[index] == value:
            filtered.append(el)
    return filtered



if __name__ == '__main__':
    #print(calculate_power_consumption('resources/inputs/day3/day3.txt', 12))
    print(calculate_life_support_rating('resources/inputs/day3/day3.txt', 12))

