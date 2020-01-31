class Action:
    def __init__(self, move_command, move_y, move_x):
        self.move_command = move_command
        self.move_x = move_x
        self.move_y = move_y

    def new_position(self, position):
        return position[0] + self.move_y, position[1] + self.move_x

    def __str__(self):
        return self.move_command

    def __repr__(self):
        return self.move_command
