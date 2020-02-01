import numpy as np
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action
from collections import defaultdict
from rl.gridworld.utils import *
import seaborn as sns

def play_game(grid, policy):
    """
    :param grid: a game board
    :param policy: how an agent will interact with the grid given the state.
    :return: return a list of states and correspending returns
    """
    alpha = 0.9
    grid.reset_board()
    states_actions_rewards = [(grid.pos, policy[grid.pos], 0)]
    previous_position = None
    while not grid.is_over:
        action_to_take = policy[grid.pos] if grid.pos in policy else np.random.choice(grid.possible_actions())
        reward = grid.player_take_action(action_to_take)
        states_actions_rewards.append((grid.pos, action_to_take, reward if previous_position != grid.pos else -100))
        previous_position = grid.pos

    G = 0
    states_actions_returns = []
    for (state, action, reward) in reversed(states_actions_rewards):
        G = reward + alpha * G
        states_actions_returns.append((state, action, G))
    return list(reversed(states_actions_returns))[1:]



if __name__ == "__main__":
    grid = standard_grid(success_prob=0.8)
    states = grid.all_states()
    possible_states = [s for s in states if not grid.is_terminal_state(s)]

    # Initialize V
    print("Initialize steps")
    alpha = 0.9
    epsilon = 10e-4
    iterations = 0
    Q = defaultdict(int)
    counts= defaultdict(lambda: 1)
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

    # print_values(Q, grid)
    print("Start playing games")

    game_nums = 500
    deltas = []

    for i in range(game_nums):
        iterations += 1
        states_actions_returns = play_game(grid, policy)

        # Policy evaluation
        seen_state_actions = {}
        max_difference = -math.inf
        for (state, action, return_g) in states_actions_returns:
            sa = (state, action)
            if sa in seen_state_actions:
                pass
            old_q = Q[sa]
            counts[sa]+=1
            Q[sa] = (Q[sa] * (counts[sa] - 1) + return_g) / counts[sa]
            seen_state_actions = sa
            max_difference = max(max_difference, abs(old_q - Q[sa]))
        deltas.append(max_difference)
        # Policy extraction
        for s in possible_states:
            grid.set_player_position(s)
            possible_actions = grid.possible_actions()

            max_action = None
            max_reward = -math.inf
            for a in possible_actions:
                q = Q[(s, a)]
                if q > max_reward:
                    max_reward = q
                    max_action = a

            policy[s] = max_action
        print_policy(policy, grid)

print("policy:")
print_policy(policy, grid)
print("Iterations: %d"%iterations)


sns.lineplot(deltas)
