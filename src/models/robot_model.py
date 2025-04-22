from enum import Enum


class Directions(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    @classmethod
    def turn_left(cls, current):
        return Directions((current.value + 1) % 4)

    @classmethod
    def turn_right(cls, current):
        return Directions((current.value - 1) % 4)


class RobotModel:
    def __init__(self, x, y, direction=Directions.RIGHT):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        self.direction = Directions.turn_left(self.direction)

    def turn_right(self):
        self.direction = Directions.turn_right(self.direction)

    def move_forward(self):
        if self.direction == Directions.UP:
            self.y -= 1
        elif self.direction == Directions.DOWN:
            self.y += 1
        elif self.direction == Directions.LEFT:
            self.x -= 1
        elif self.direction == Directions.RIGHT:
            self.x += 1
