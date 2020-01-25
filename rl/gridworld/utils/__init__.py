from rl.gridworld.Grid import Grid
from rl.gridworld.entity.Player import Player
from rl.gridworld.entity.Reward import Reward
from rl.gridworld.entity.Block import Block
from rl.gridworld.Action import Action


def standard_grid(success_prob = 1.0, normal_reward = 0.0):
    p1 = Player("A")
    grid = Grid(3, 4, p1, (2, 3), success_prob = success_prob, normal_reward=normal_reward)
    rewards = {
        (0, 3): Reward(1, is_terminal=True), (1, 3): Reward(-1, is_terminal=True)
    }
    blocks = {
        (1, 1): Block()
    }

    grid.set_board(rewards, blocks)
    return grid

def print_values(V, grid):
    print("="*10)
    for i in range(grid.height):
        for j in range(grid.width):
            v = V.get((i, j), 0)
            if v >= 0:
                print(" %.2f|" % v, end='')
            else:
                print("%.2f|" % v, end='')
        print("")
    print("="*10)

def print_policy(P, grid):
    print("="*10)
    for i in range(grid.height):
        for j in range(grid.width):
            a = P.get((i, j), Action(" ", 0, 0)).move_command
            print(" %s |" % a, end='')
        print("")
    print("="*10)
