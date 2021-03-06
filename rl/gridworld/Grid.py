import numpy as np
from rl.gridworld.Action import Action
import os
import random
from itertools import product
from copy import deepcopy

basic_actions = [
    Action("U", -1, 0),
    Action("D", 1, 0),
    Action("L", 0, -1),
    Action("R", 0, 1),
]


class Grid:
    def __init__(self, height, width, player, pos, success_prob=1.0, normal_reward = 0):
        self.width = width
        self.height = height
        self.entity = {}
        self.pos = pos
        self.starting_pos = deepcopy(pos)
        self.player = player
        self.is_over = False
        self.success_prob = success_prob
        self.normal_reward = normal_reward

    def get_current_position(self):
        return deepcopy(self.pos)

    def reset_board(self):
        self.pos =self.starting_pos
        self.is_over = False
        # Make non-terminal reward reappear too, pls

    def set_board(self, rewards, blocks):
        self.entity = {**rewards, **blocks}
        return True

    def draw_board(self):
        print("=" * 50)
        for h in range(self.height):
            for w in range(self.width):
                entity_at_position = "."
                if (h, w) == self.pos:
                    entity_at_position = self.player.character()
                elif (h, w) in self.entity:
                    entity_at_position = self.entity[(h, w)].character()
                # else:
                print(" {} ".format(entity_at_position), end="")
            print()

    def all_states(self):
        return [(i, j) for i, j in product(range(self.height), range(self.width)) if
                self.is_valid_position((i, j))]

    def possible_actions(self):
        possible_actions = []
        for action in basic_actions:
            new_position = action.new_position(self.pos)
            if self.is_valid_position(new_position):
                possible_actions.append(action)
        return possible_actions

    def is_valid_position(self, position):
        (x, y) = position
        if x < 0 or x >= self.height:
            return False  # Going against Wall
        if y < 0 or y >= self.width:
            return False  # Going against Wall

        if position in self.entity:
            return self.entity[position].can_interact(self.player)
        else:
            return True

    def player_take_action(self, action):
        # Randomness
        randomed_action = action
        if random.random() >= self.success_prob:
            other_actions = [a for a in self.possible_actions() if a.move_command != action.move_command]
            randomed_action = np.random.choice(other_actions)

        # Start moving
        new_position = randomed_action.new_position(self.pos)
        reward = self.normal_reward
        if self.is_valid_position(new_position):
            if new_position in self.entity:
                e = self.entity[new_position]
                reward += e.interact(self.player)
                if e.is_terminal:
                    self.is_over = True
                else:
                    del self.entity[new_position]
            self.pos = new_position
            return reward
        else:
            raise Exception("Invalid Move!!")

    def set_player_position(self, position):
        self.pos = position

    def is_terminal_state(self, position):
        return position in self.entity and self.entity[position].is_terminal