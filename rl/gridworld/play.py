from rl.gridworld.Grid import Grid
from rl.gridworld.entity.Player import Player
from rl.gridworld.entity.Reward import Reward
from rl.gridworld.entity.Block import Block

if __name__ == '__main__':
    p1 = Player("A")
    grid = Grid(3, 4, p1, (2, 3))
    rewards = {
        (0, 3): Reward(1), (1, 3): Reward(-1)
    }
    blocks = {
        (1, 1): Block()
    }

    grid.set_board(rewards, blocks)
    grid.draw_board()
