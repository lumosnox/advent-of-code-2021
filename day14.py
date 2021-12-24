
# Part 1
import copy
import sys


def calculate_part1(filename, steps):
    rules = {}
    occurrences = {}
    # process input
    with open(filename) as file:
        template = file.readline().rstrip()
        file.readline()
        for line in file:
            pair, elem = line.rstrip().split(' -> ')
            rules[pair] = elem

    chain = apply_rules(template, steps, rules)

    calculate_occurrences(chain, occurrences)

    min, max = calculate_min_max(occurrences)

    return max - min


def apply_rules(template, steps, rules):
    chain = copy.deepcopy(template)
    for step in range(0, steps):
        next_step_chain = []
        l = len(chain)
        for i in range(0, l-1):
            next_step_chain.append(chain[i])
            rule = rules[''.join(chain[i:i+2])]
            if rule:
                next_step_chain.append(rule)
        next_step_chain.append(chain[l-1])
        chain = copy.deepcopy(next_step_chain)
    return chain


def calculate_occurrences(chain, occurences):
    for i in range(0, len(chain)):
        if chain[i] in occurences:
            occurences[chain[i]] = occurences[chain[i]] + 1
        else:
            occurences[chain[i]] = 1


def calculate_min_max(dict):
    min = sys.maxsize
    max = -1
    for key, value in dict.items():
        if value > max:
            max = value
        if value < min:
            min = value
    return min, max


if __name__ == '__main__':
    print(calculate_part1('resources/inputs/day14/day14.txt', 10))

