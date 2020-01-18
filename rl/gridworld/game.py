from rl.gridworld.Grid import Grid
from rl.gridworld.entity.Player import Player
from rl.gridworld.entity.Reward import Reward
from rl.gridworld.entity.Block import Block


def play_game(grid):
    while not grid.is_over:
        grid.draw_board()
        possible_actions = grid.possible_actions()
        action_string = [a.move_command for a in possible_actions]
        moving = []
        while len(moving) == 0:
            move = input("Move (%s): "%",".join(action_string))
            moving = [action for action in possible_actions if action.move_command == move]

        grid.player_take_action(moving[0])
    print(grid.reward)


if __name__ == '__main__':
    p1 = Player("A")
    grid = Grid(3, 4, p1, (2, 3))
    rewards = {
        (0, 3): Reward(1, True), (1, 3): Reward(-1)
    }
    blocks = {
        (1, 1): Block()
    }

    grid.set_board(rewards, blocks)
    play_game(grid)
