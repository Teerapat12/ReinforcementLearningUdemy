from rl.gridworld.entity.EntityBase import EntityBase


class Reward(EntityBase):
    def __init__(self, score, is_terminal=False):
        super().__init__()
        self.score = score
        self.is_terminal = is_terminal

    def character(self):
        if self.score > 0:
            return "O"
        else:
            return "X"

    def can_interact(self, other):
        return True

    def interact(self, other):
        return self.score