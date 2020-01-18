from rl.gridworld.Action import Action
import os

basic_actions = [
    Action("U", -1, 0),
    Action("D", 1, 0),
    Action("L", 0, -1),
    Action("R", 0, 1),
]


class Grid:
    def __init__(self, height, width, player, pos):
        self.width = width
        self.height = height
        self.entity = {}
        self.pos = pos
        self.player = player
        self.is_over = False
        self.reward = 0

    def set_board(self, rewards, blocks):
        self.entity = {**rewards, **blocks}
        return True

    def draw_board(self):
        print("=" * 50)
        for h in range(self.height):
            for w in range(self.width):
                entity_at_position = "."
                if (h, w) == self.pos:
                    entity_at_position = self.player.character()
                elif (h, w) in self.entity:
                    entity_at_position = self.entity[(h, w)].character()
                # else:
                print(" {} ".format(entity_at_position), end="")
            print()

    def possible_actions(self):
        possible_actions = []
        for action in basic_actions:
            new_position = action.new_position(self.pos)
            if self.is_valid_position(new_position):
                possible_actions.append(action)
        return possible_actions

    def is_valid_position(self, position):
        (x, y) = position
        if x < 0 or x >= self.height:
            return False  # Going against Wall
        if y < 0 or y >= self.width:
            return False  # Going against Wall

        if position in self.entity:
            return self.entity[position].can_interact(self.player)
        else:
            return True

    def player_take_action(self, action):
        new_position = action.new_position(self.pos)
        if self.is_valid_position(new_position):
            if new_position in self.entity:
                e = self.entity[new_position]
                self.reward += e.interact(self.player)
                if e.is_terminal:
                    self.is_over = True
                del self.entity[new_position]
            self.pos = new_position
        else:
            raise Exception("Invalid Move!!")
