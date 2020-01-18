import numpy as np
def calculate_is_end(board):
    if np.count_nonzero(board) == 9:
        return 0

    for i in [0, 1, 2]:
        is_win_by_row = (
        board[i][0] != 0 and board[i][0] == board[i][1] and board[i][1] == board[i][2])
        is_win_by_col = (
        board[0][i] != 0 and board[0][i] == board[1][i] and board[1][i] == board[2][i])
        if is_win_by_col:
            return board[0][i]
        if is_win_by_row:
            return board[i][0]

    if (board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
            (board[2][0] != 0 and board[2][0] == board[1][1] and board[1][1] == board[0][
                2]):
        return board[1][1]
    return -1

def calculate_board_reward(board, player_index):
    winner = calculate_is_end(board)
    if winner == player_index:
        return 1
    elif winner == 0 or winner == -1:  # Not finished (-1), Draw (0)
        return 0
    else:
        return -1

def calculate_potential_board_reward(board, x, y, player_index):
    tmp = board.copy()
    tmp[x][y] = player_index
    return calculate_board_reward(tmp, player_index)