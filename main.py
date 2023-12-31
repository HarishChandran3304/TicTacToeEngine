from game import print_board, check_win, check_draw
from pruning import get_turn, get_actions, result, get_score, minimaxABP


def main():
    board = [[None for _ in range(3)] for _ in range(3)]
    winner = None
    turns = ["X", "O"]
    print_board(board)
    for i in range(9):
        turn = get_turn(board)
        if turn == "X":
            row, col = map(int, input("Your turn: ").split())
            board[row-1][col-1] = "X"

        else:
            actions = get_actions(board)
            scores = []
            for action in actions:
                scores.append(minimaxABP(result(board, action), 1, float("-inf"), float("+inf")))
            row, col = actions[scores.index(max(scores))]
            board[row][col] = "O" 
            print(f'Engine plays: {row+1} {col+1}')
        print_board(board)

        if winner := check_win(board):
            print(f'{winner} wins!')
            break
        
        if check_draw(board):
            print("Draw!")
            break


if __name__ == "__main__":
    main()
