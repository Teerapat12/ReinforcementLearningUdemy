from rl.gridworld.Grid import Grid
from rl.gridworld.entity.Player import Player
from rl.gridworld.entity.Reward import Reward
from rl.gridworld.entity.Block import Block
from itertools import product
import math
from rl.gridworld.utils import standard_grid
from rl.gridworld.Action import Action

def print_values(V, grid):
    for i in range(grid.height):
        for j in range(grid.width):
            v = V.get((i, j), 0)
            if v >= 0:
                print(" %.2f|" % v, end='')
            else:
                print("%.2f|" % v, end='')
        print("")


def print_policy(P, grid):
    for i in range(grid.height):
        for j in range(grid.width):
            a = P.get((i, j), Action(" ", 0, 0)).move_command
            print(" %s |" % a, end='')
        print("")


def iterative_value_evaluation(grid, gamma, epsilon):
    states = grid.all_states()
    V = {}
    biggest_change = math.inf
    while biggest_change > epsilon:
        biggest_change = -math.inf
        for s in states:
            old_v = V.get(s, 0)
            if not grid.is_terminal_state(s):
                new_v = 0
                p_a = 1.0 / len(grid.possible_actions())
                grid.set_player_position(s)
                possible_actions = grid.possible_actions()
                for a in possible_actions:
                    grid.set_player_position(s)
                    r = grid.player_take_action(a)
                    new_v += p_a * (r + gamma * V.get(grid.pos, 0))
                # print(new_v)
                V[s] = new_v
                biggest_change = max(biggest_change, abs(old_v - V[s]))
        print_values(V, grid)
        print("+++")

policy_1 =  {
    (2, 0 ): Action("U", -1, 0),
    (1, 0): Action("U", -1, 0),
    (0, 0): Action("R", 0, 1),
    (0, 1): Action("R", 0, 1),
    (0, 2): Action("R", 0, 1),
    (1, 2): Action("R", 0, 1),
    (2, 1): Action("R", 0, 1),
    (2, 2): Action("R", 0, 1),
    (2, 3): Action("U", -1, 0),
}

def fix_policy_iterative_value_evaluation(grid, gamma, epsilon, policy):
    print_policy(policy, grid)
    states = grid.all_states()
    V = {}
    biggest_change = math.inf
    while biggest_change > epsilon:
        biggest_change = -math.inf
        for s in states:
            old_v = V.get(s,0)
            if not grid.is_terminal_state(s):
                new_v = 0
                action = policy[s]
                grid.set_player_position(s)
                r = grid.player_take_action(action)
                V[s] = r + gamma * V.get(grid.pos, 0)
                biggest_change = max(biggest_change, abs(old_v - V[s]))
        print_values(V, grid)
        print("+++")
    print(V)



if __name__ == "__main__":
    grid = standard_grid()
    states = grid.all_states()
    # iterative_value_evaluation(grid, 1.0, 10e-2)
    fix_policy_iterative_value_evaluation(grid, 0.9, 10e-4, policy_1)
