import copy
import time


# Part 1
def calculate_part1(filename, days):
    with open(filename) as file:
        fish = [int(x) for x in file.readline().split(',')]
    return len(simulate_lanternfish(fish, days))


def simulate_lanternfish(fish, days):
    fish_simulation = copy.deepcopy(fish)
    for day in range(1, days + 1):
        new_fish_counter = 0
        for i, timer in enumerate(fish_simulation):
            timer = timer - 1
            if timer == -1:
                timer = 6
                new_fish_counter = new_fish_counter + 1
            fish_simulation[i] = timer
        fish_simulation.extend([8] * new_fish_counter)
    return fish_simulation


if __name__ == '__main__':
    start_time = time.time()
    days_to_simulate = 80
    print(calculate_part1('resources/inputs/day6/day6.txt', days_to_simulate))
