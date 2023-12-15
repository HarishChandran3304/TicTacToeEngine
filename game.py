def print_board(board):
    for row in board:
        print(row)
    print()

def check_rows(board):
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    return None

def check_cols(board):
    for i in range(3):
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    return None

def check_diags(board):
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def check_win(board):
    if winner := check_rows(board):
        return winner
    
    if winner := check_cols(board):
        return winner
    
    if winner := check_diags(board):
        return winner
    
    return None

def check_draw(board):
    if all([all(row) for row in board]):
        return True
    return False

