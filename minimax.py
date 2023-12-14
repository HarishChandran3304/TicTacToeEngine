from game import check_winner, check_draw

def is_terminal(board):
    return True if check_winner(board) or check_draw(board) else False

def get_score(board):
    if check_winner(board) == "O":
        return 1

    if check_winner(board) == "X":
        return -1
    
    if check_draw(board):
        return 0

def get_turn(board):
    return "O" if sum([row.count("X") for row in board]) > sum([row.count("O") for row in board])

def get_actions(board):
    actions = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.append((i, j))

    return actions

