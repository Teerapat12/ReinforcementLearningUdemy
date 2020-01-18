import random

class Player:
    def __init__(self, p_index):
        self.player_character = p_index


    def play_game(self, board):
        print(board.get_board())
        x, y = [int(x) for x in input("Enter x, y: ").split()]
        return board.update_game(x, y, self.player_character)

    def update_state_history(self, board):
        return True

    def update_state_value_maps(self, board):
        return True
