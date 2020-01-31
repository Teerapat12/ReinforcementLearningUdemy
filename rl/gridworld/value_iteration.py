import numpy as np
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action
from collections import defaultdict
from rl.gridworld.utils import *
if __name__ == "__main__":
    grid = standard_grid(normal_reward=-0.1)
    states = grid.all_states()
    possible_states = [s for s in states if not grid.is_terminal_state(s)]

    # Initialize V
    print("Initialize steps")
    alpha = 0.9
    epsilon = 10e-4
    iterations = 0
    V = {state: 0 for state in states}

    print_values(V, grid)
    # repeat until policy converged

    # value iteration
    while True:
        iterations += 1
        biggest_change = -math.inf
        for state in possible_states:
            old_v = V[state]
            grid.set_player_position(state)
            new_v = -math.inf
            for action in grid.possible_actions():
                grid.set_player_position(state)
                reward = grid.player_take_action(action)
                new_v = max(reward + alpha * V[grid.pos], new_v)
            V[state] = new_v
            biggest_change = max(abs(V[state] - old_v), biggest_change)
        print_values(V, grid)
        if biggest_change < epsilon:
            print_values(V, grid)
            break

    # policy extraction
    policy = {}
    for state in possible_states:
        grid.set_player_position(state)
        possible_actions = grid.possible_actions()

        new_action = None
        best_value = -math.inf
        for action in possible_actions:
            grid.set_player_position(state)
            reward = grid.player_take_action(action)
            v = reward + alpha * V[grid.pos]
            if v > best_value:
                best_value = v
                new_action = action
        policy[state] = new_action

    print_policy(policy, grid)

print("values:")
print_values(V, grid)
print("policy:")
print_policy(policy, grid)
print("Iterations: %d"%iterations)