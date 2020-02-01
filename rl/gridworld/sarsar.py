import numpy as np
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action
from collections import defaultdict
from rl.gridworld.utils import *
import seaborn as sns
import random


def epsilon_greedy_from(Q, s, possible_actions, epsilon):
    p = random.random()
    if p < epsilon:
        return np.random.choice(possible_actions)
    else:
        max_action = None
        max_val = -math.inf
        for a in possible_actions:
            if Q[(s, a)] > max_val:
                max_val = Q[(s,a)]
                max_action = a
        return max_action


if __name__ == "__main__":
    grid = standard_grid(success_prob=0.8)
    states = grid.all_states()
    possible_states = [s for s in states if not grid.is_terminal_state(s)]

    # Initialize V
    print("Initialize steps")
    alpha = 0.9
    epsilon = 10e-4
    iterations = 0
    Q = defaultdict(lambda: 0)
    counts= defaultdict(lambda: 1)

    # print_values(Q, grid)
    print("Start playing games")

    game_nums = 500
    alpha = 0.1 # Learning rate
    gamma = 0.2 # Discount factor
    epsilon = 1
    deltas = []



    for i in range(game_nums):
        iterations += 1
        grid.reset_board()
        state = grid.get_current_position()
        possible_actions = grid.possible_actions()
        action = epsilon_greedy_from(Q, state, possible_actions, 1.0/(i+1.0))

        while not grid.is_over:
            reward = grid.player_take_action(action)
            state_new = grid.get_current_position()

            # Do action
            possible_actions = grid.possible_actions()
            action_new = epsilon_greedy_from(Q, state_new, possible_actions, 1.0/(i+1.0))

            old_sa = (state, action)
            sa = (state_new, action_new)
            Q[old_sa] = Q[old_sa] + alpha * (reward + gamma *  Q[sa])
            state = state_new
            action = action_new


print("policy:")
print_policy(policy, grid)
print("Iterations: %d"%iterations)


sns.lineplot(deltas)
