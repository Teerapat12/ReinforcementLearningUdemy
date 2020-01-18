from rl.gridworld.entity.EntityBase import EntityBase


class Player(EntityBase):

    def __init__(self, char):
        super(Player, self).__init__()
        self.char = char

    def character(self):
        return self.char

    def can_interact(self, other):
        if isinstance(other, Player):
            return False
        else:
            return True
