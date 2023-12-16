from copy import deepcopy
from game import check_win, check_draw

def is_terminal(board):
    return True if check_win(board) or check_draw(board) else False

def get_score(board):
    if check_win(board) == "O":
        return 1

    if check_win(board) == "X":
        return -1
    
    if check_draw(board):
        return 0

def get_turn(board):
    return "O" if sum([row.count("X") for row in board]) > sum([row.count("O") for row in board]) else "X"

def get_actions(board):
    actions = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.append((i, j))

    return actions

def result(board, action):
    board = deepcopy(board)
    board[action[0]][action[1]] = get_turn(board)
    return board

def minimax(board):
    if is_terminal(board):
        return get_score(board)

    if get_turn(board) == "O":
        score = float("-inf")
        for action in get_actions(board):
            score = max(score, minimax(result(board, action)))
        return score

    if get_turn(board) == "X":
        score = float("inf")
        for action in get_actions(board):
            score = min(score, minimax(result(board, action)))
        return score

