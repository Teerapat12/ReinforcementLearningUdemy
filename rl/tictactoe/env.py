import numpy as np
from rl.tictactoe.board_util import calculate_is_end, calculate_board_reward
class TicTacToeEnv:
    def __init__(self):
        self.boards = np.zeros((3,3))

    def check_is_end(self):
        return calculate_is_end(self.boards)

    def calculate_reward(self, player_index):
        return calculate_board_reward(self.boards, player_index)

    def update_game(self, x, y, player):
        if self.boards[x][y]!=0:
            return False
        self.boards[x][y] = player
        return True

    def get_board(self):
        return self.boards

    def get_board_as_string(self):
        return np.array2string(self.boards)

    def get_potential_board_as_string(self, x, y, player):
        tmp = self.boards.copy()
        tmp[x][y] = player
        return np.array2string(tmp)

    def reset_board(self):
        self.boards = np.zeros((3,3))

    def get_free_positions(self):
        # Sry too lazy to write nicely
        result = []
        for i in range(3):
            for j in range(3):
                if self.boards[i][j]==0:
                    result.append((i,j))
        assert len(result)>0, "The board is full!"
        return result



game = TicTacToeEnv()
game.update_game(0,0, 1)
game.update_game(0,1, 1)
assert(list(game.get_board()[0]) == [1,1,0])
assert(list(game.get_board()[1]) == [0,0,0])
assert(game.check_is_end() == -1)
game.update_game(0,2, 1)
assert(game.check_is_end() == 1)
