import numpy as np
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action
from collections import defaultdict
from rl.gridworld.utils import *
if __name__ == "__main__":
    grid = standard_grid(0.5, -0.1)
    states = grid.all_states()
    possible_states = [s for s in states if not grid.is_terminal_state(s)]

    # Initialize V, policy
    print("Initialize steps")
    alpha = 0.9
    epsilon = 10e-4
    V = {state: 0 for state in states}


    policy = {}
    for state in possible_states:
        grid.set_player_position(state)
        policy[state] = np.random.choice(grid.possible_actions())

    print_values(V, grid)
    print_policy(policy, grid)

    # repeat until policy converged

    while True:

        # policy evaluation
        while True:
            biggest_change = -math.inf
            for state in possible_states:
                old_v = V[state]
                action = policy[state]
                grid.set_player_position(state)
                reward = grid.player_take_action(action)
                V[state] = reward + alpha * V[grid.pos]
                biggest_change = max(abs(V[state] - old_v), biggest_change)

            if biggest_change < epsilon:
                print_values(V, grid)
                break

        # policy improvement steps
        is_policy_converged = True
        for state in possible_states:
            current_v = V[state]
            old_action = policy[state]

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

            if new_action != old_action:
                is_policy_converged = False

        print_policy(policy, grid)
        if is_policy_converged:
            break

print("values:")
print_values(V, grid)
print("policy:")
print_policy(policy, grid)