import numpy as np
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action
from collections import defaultdict
from rl.gridworld.utils import *

def play_game(grid, policy):
    """
    :param grid: a game board
    :param policy: how an agent will interact with the grid given the state.
    :return: return a list of states and correspending returns
    """
    alpha = 0.9
    grid.reset_board()
    state_and_rewards = [(grid.pos, 0)]
    while not grid.is_over:
        action_to_take = policy[grid.pos] if grid.pos in policy else np.random.choice(grid.possible_actions())
        reward = grid.player_take_action(action_to_take)
        state_and_rewards.append((grid.pos, reward))

    G = 0
    states_and_returns = []
    for (state, reward) in reversed(state_and_rewards):
        G = reward + alpha * G
        states_and_returns.append((state, G))
    return list(reversed(states_and_returns))[1:]



if __name__ == "__main__":
    grid = standard_grid(success_prob=0.8)
    states = grid.all_states()
    possible_states = [s for s in states if not grid.is_terminal_state(s)]

    # Initialize V
    print("Initialize steps")
    alpha = 0.9
    epsilon = 10e-4
    iterations = 0
    V = {state: 0 for state in states}
    counts= {state: 1 for state in states}
    policy = {
        (2, 0): Action("U", -1, 0),
        (1, 0): Action("U", -1, 0),
        (0, 0): Action("R", 0, 1),
        (0, 1): Action("R", 0, 1),
        (0, 2): Action("R", 0, 1),
        (1, 2): Action("R", 0, 1),
        (2, 1): Action("R", 0, 1),
        (2, 2): Action("U", -1, 0),
        (2, 3): Action("L", 0, -1),
    }

    print_values(V, grid)
    print("Start playing games")

    game_nums = 5

    for i in range(game_nums):
        states_and_returns = play_game(grid, policy)
        for (state, return_g) in states_and_returns:
            old_v = V[state]
            counts[state]+=1
            V[state] = (V[state] * (counts[state]-1) + return_g) / counts[state]

print("values:")
print_values(V, grid)
print("policy:")
print_policy(policy, grid)
print("Iterations: %d"%iterations)