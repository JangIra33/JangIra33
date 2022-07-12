import random

def initialize_board_9x9():
    row0 = [1, 2, 3, 4,5,6,7,8,9]
    random.shuffle(row0)
    row1 = [row0[4], row0[7], row0[6], row0[5], row0[3], row0[8], row0[2], row0[1], row0[0]]
    row2 = [row0[7], row0[0], row0[3], row0[6], row0[5], row0[2], row0[8], row0[4], row0[1]]
    row3 = [row0[6], row0[2], row0[4], row0[0], row0[1], row0[7], row0[5], row0[8], row0[3]]
    row4 = [row0[5], row0[6], row0[7], row0[8], row0[2], row0[3], row0[1], row0[0], row0[4]]
    row5 = [row0[8], row0[3], row0[1], row0[2], row0[0], row0[6], row0[4], row0[5], row0[7]]
    row6 = [row0[3], row0[5], row0[8], row0[4], row0[7], row0[1], row0[0], row0[2], row0[6]]
    row7 = [row0[2], row0[8], row0[0], row0[1], row0[6], row0[4], row0[7], row0[3], row0[5]]
    row8 = [row0[1], row0[4], row0[5], row0[7], row0[8], row0[0], row0[3], row0[6], row0[2]]
    board = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
    return board

def shuffle_ribbons(board):
    top = board[:3]
    mid = board[3:6]
    bottom = board[6:]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    return top + mid + bottom

def transpose(board):
    size = len(board)
    transposed = []
    for _ in range(size):
        transposed.append([])
    for row in board:
        for j in range(size):
            transposed[j].append(row[j])
    return transposed

def create_solution_board_9x9():
    board = initialize_board_9x9()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board :
        board_clone.append(row[:])
    return board_clone

def get_level():
    level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요 : ")
    while level not in ("1","2","3"):
        level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요 : ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def get_integer(message,i,j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

def sudoku_mini():
    solution_board = create_solution_board_9x9()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~9): ",1,9) - 1
        j = get_integer("세로줄번호(1~9): ",1,9) - 1
        if puzzle_board[i][j] != 0:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~9): ",1,9)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n,"가(이) 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")

sudoku_mini()