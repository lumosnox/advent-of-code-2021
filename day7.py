#  Woo! Quickest advent day! Around 15 mins :)

# Part 1
def calculate_part1(filename):
    with open(filename) as file:
        crabs_positions = [int(x) for x in file.readline().split(',')]
    max_crab_position = max(crabs_positions)
    fuel_spend = []
    for pos in range(0, max_crab_position + 1):
        fuel = 0
        for crab_pos in crabs_positions:
            fuel = fuel + abs(crab_pos - pos)
        fuel_spend.append(fuel)
    return min(fuel_spend)


# Part 2
def calculate_part2(filename):
    with open(filename) as file:
        crabs_positions = [int(x) for x in file.readline().split(',')]
    max_crab_position = max(crabs_positions)
    fuel_spend = []
    initialize_fuel_cache()
    for pos in range(0, max_crab_position + 1):
        fuel = 0
        for crab_pos in crabs_positions:
            diff = abs(crab_pos - pos)
            fuel = fuel + calc_fuel(diff)
        fuel_spend.append(fuel)
    return min(fuel_spend)


fuel_cache = []


def initialize_fuel_cache():
    for i in range(0, 1000000):
        fuel_cache.append(-1)


def calc_fuel(diff):
    if fuel_cache[diff] != -1:
        return fuel_cache[diff]
    fuel = 0
    for i in range(1, diff + 1):
        fuel = fuel + i
    fuel_cache[diff] = fuel
    return fuel


if __name__ == '__main__':
    #print(calculate_part1('resources/inputs/day7/day7.txt'))
    print(calculate_part2('resources/inputs/day7/day7.txt'))

