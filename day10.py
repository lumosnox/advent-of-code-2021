
# Part 1
import copy


def calculate_part1(filename):
    score = 0
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    with open(filename) as file:
        for line in file:
            corrupter_char = find_corrupted_character(line.rstrip())
            if corrupter_char is not None:
                score = score + score_map[corrupter_char]
    return score


def find_corrupted_character(line):
    no_more_changes_to_make = False
    while (')' in line or ']' in line or '}' in line or '>' in line) and not no_more_changes_to_make:
        initial_line = copy.deepcopy(line)
        line = line.replace('()', '')
        line = line.replace('[]', '')
        line = line.replace('{}', '')
        line = line.replace('<>', '')
        if initial_line == line:
            no_more_changes_to_make = True
    for c in line:
        if c in [')', ']', '}', '>']:
            return c
    return None


# Part 2
closing_tag = {'(': ')', '[': ']', '{': '}', '<': '>'}
completion_tag_score = {')': 1, ']': 2, '}': 3, '>': 4}


def calculate_part2(filename):
    scores = []
    with open(filename) as file:
        for line in file:
            score = autocomplete_line_score(line.rstrip())
            if score is not None:
                scores.append(score)
    middle = len(scores) // 2
    return sorted(scores)[middle]


def autocomplete_line_score(line):
    no_more_changes_to_make = False
    while (')' in line or ']' in line or '}' in line or '>' in line) and not no_more_changes_to_make:
        initial_line = copy.deepcopy(line)
        line = line.replace('()', '')
        line = line.replace('[]', '')
        line = line.replace('{}', '')
        line = line.replace('<>', '')
        if initial_line == line:
            no_more_changes_to_make = True
    correct_sequence = []
    score = 0
    for c in reversed(line):
        if c in [')', ']', '}', '>']:
            return None  # is corrupt
        else:
            score = score*5 + completion_tag_score[closing_tag[c]]
            correct_sequence.append(closing_tag[c])
    if score != 0:
        return score
    return None


if __name__ == '__main__':
    print(calculate_part2('resources/inputs/day10/day10.txt'))

