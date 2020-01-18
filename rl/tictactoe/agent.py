import random
import numpy as np
from rl.tictactoe.board_util import calculate_is_end, calculate_board_reward, calculate_potential_board_reward

class Agent:
    def __init__(self, p_index):
        self.player_character = p_index
        self.state_value_map = dict()
        self.epsilon = 0.1
        self.learning_rate = 0.2
        self.episode_states_history = []

    def play_game(self, board):
        sample = random.random()
        if sample<self.epsilon:
            # Explore
            x,y = random.choice(board.get_free_positions())
        else:
            all_free_positions = board.get_free_positions()
            all_possible_states = [board.get_potential_board_as_string(x,y,self.player_character) for x,y in all_free_positions]
            all_states_value = [self.get_state_value(state, board, future_x, future_y) for state, (future_x, future_y) in zip(all_possible_states, all_free_positions)]

            max_state_index = np.argmax(all_states_value)
            x,y = all_free_positions[max_state_index]

        return board.update_game(x, y, self.player_character)

    def get_state_value(self, state_str, board, x, y):
        if state_str not in self.state_value_map:
            self.state_value_map[state_str] = calculate_potential_board_reward(board.get_board(), x, y, self.player_character)
        return self.state_value_map[state_str]

    def update_state_history(self, board):
        board_as_string = board.get_board_as_string()
        self.episode_states_history.append(board.get_board_as_string())

        # Also update states_value_map if unknown as we know how.
        self.initialize_unknown_state_value(board, board_as_string)
        return True

    def initialize_unknown_state_value(self, board, board_as_string):
        if board_as_string not in self.state_value_map:
            self.state_value_map[board_as_string] = board.calculate_reward(self.player_character)

    def update_state_value_maps(self, board):
        self.episode_states_history.reverse()
        new_value = board.calculate_reward(self.player_character)
        for history_state in self.episode_states_history:
            old_value = self.state_value_map[history_state]
            self.state_value_map[history_state]  =  old_value + self.learning_rate * (new_value - old_value)
            new_value = self.state_value_map[history_state]
        self.reset_state_history()
        return True


    def reset_state_history(self):
        self.episode_states_history = []
        return True


    def save_state(self, name):
        np.save(name, self.state_value_map)

    def load_state(self, name):
        self.state_value_map = np.load(name, allow_pickle=True).item()
