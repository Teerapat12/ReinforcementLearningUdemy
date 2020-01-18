import random

class RandomAgent:
    def __init__(self, p_index):
        self.player_character = p_index


    def play_game(self, board):
        x, y = random.choice(board.get_free_positions())
        return board.update_game(x, y, self.player_character)

    def update_state_history(self, board):
        return True

    def update_state_value_maps(self, board):
        return True
