from enum import Enum


class Directions(Enum):
    """Перелічення напрямків."""
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    @classmethod
    def turn_left(cls, current):
        """Повертає ліворуч."""
        return Directions((current.value + 1) % 4)

    @classmethod
    def turn_right(cls, current):
        """Повертає праворуч."""
        return Directions((current.value - 1) % 4)


class RobotModel:
    def __init__(self, x, y, direction=Directions.RIGHT):
        """Приймає параметри."""
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        """Визиває поворот ліворуч."""
        self.direction = Directions.turn_left(self.direction)

    def turn_right(self):
        """Визиває поворот праворуч."""
        self.direction = Directions.turn_right(self.direction)

    def move_forward(self):
        """Змінює положення за напрямком."""
        if self.direction == Directions.UP:
            self.y -= 1
        elif self.direction == Directions.DOWN:
            self.y += 1
        elif self.direction == Directions.LEFT:
            self.x -= 1
        elif self.direction == Directions.RIGHT:
            self.x += 1
