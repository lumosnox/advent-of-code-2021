
# Part 1
def calculate_part1(filename):
    with open(filename) as file:
        line1 = file.readline()
        numbers_drawn = [int(x) for x in line1.split(',')]
        boards = []
        while True:
            file.readline()  # remove separator
            # read a board
            line = file.readline()
            if not line:
                break
            board = [[], [], [], [], []]
            board[0] = [int(x) for x in line.split()]
            board[1] = [int(x) for x in file.readline().split()]
            board[2] = [int(x) for x in file.readline().split()]
            board[3] = [int(x) for x in file.readline().split()]
            board[4] = [int(x) for x in file.readline().split()]
            boards.append(board)
        winner_board, last_number = calculate_bingo_winner(numbers_drawn, boards)

    return calculate_score(winner_board, last_number)


def calculate_bingo_winner(numbers_drawn, boards):
    for number in numbers_drawn:
        for board in boards:
            for row in board:
                mark_row(row, number)
            if is_bingo(board):
                return board, number


def mark_row(row, number):
    for i in range(0, 5):
        if row[i] == number:
            row[i] = -1
    return


def is_horizontal_bingo(board):
    for row in board:
        bingo = True
        for i in range(0, 5):
            if row[i] != -1:
                bingo = False
        if bingo:
            return True
    return False


def is_vertical_bingo(board):
    for col_ind in range(0, 5):
        bingo = True
        for row_ind in range(0, 5):
            if board[row_ind][col_ind] != -1:
                bingo = False
        if bingo:
            return True
    return False


def is_bingo(board):
    if not is_horizontal_bingo(board):
        return is_vertical_bingo(board)
    return True


def calculate_score(board, last_number):
    unmarked_sum = 0
    for row in board:
        for i in range(0, 5):
            if row[i] != -1:
                unmarked_sum = unmarked_sum + row[i]
    score = unmarked_sum * last_number
    return score


#####################################################

# Part 2
def calculate_part2(filename):
    with open(filename) as file:
        line1 = file.readline()
        numbers_drawn = [int(x) for x in line1.split(',')]
        boards = []
        while True:
            file.readline()  # remove separator
            # read a board
            line = file.readline()
            if not line:
                break
            board = [[], [], [], [], []]
            board[0] = [int(x) for x in line.split()]
            board[1] = [int(x) for x in file.readline().split()]
            board[2] = [int(x) for x in file.readline().split()]
            board[3] = [int(x) for x in file.readline().split()]
            board[4] = [int(x) for x in file.readline().split()]
            boards.append(board)
        winner_board, last_number = calculate_bingo_last(numbers_drawn, boards)

    return calculate_score(winner_board, last_number)


def calculate_bingo_last(numbers_drawn, boards):
    num_boards = len(boards)
    boards_that_won = []
    num_boards_that_won = 0
    for i in range(0, num_boards):
        boards_that_won.append(-1)
    for number in numbers_drawn:
        for ind, board in enumerate(boards):
            for row in board:
                mark_row(row, number)
            if is_bingo(board):
                if boards_that_won[ind] == -1:  # check this board hasn't won before
                    num_boards_that_won = num_boards_that_won + 1
                boards_that_won[ind] = 1
            if num_boards_that_won == num_boards:
                return board, number
    for i in range(0, num_boards):
        if boards_that_won[i] == -1:
            return boards[i], numbers_drawn[-1]


if __name__ == '__main__':
    #print(calculate_part1('resources/inputs/day4/day4.txt'))
    print(calculate_part2('resources/inputs/day4/day4.txt'))

