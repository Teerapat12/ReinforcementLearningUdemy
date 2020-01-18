from rl.gridworld.entity.EntityBase import EntityBase


class Block(EntityBase):
    def __init__(self):
        super().__init__()

    def character(self):
        return "B"

    def can_interact(self, other):
        return False