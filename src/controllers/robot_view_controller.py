import threading
import time

from kivy.clock import Clock

from src.models.robot_model import Directions
from src.views.cell_view import CellView


class RobotViewController:
    def __init__(self, robot_model, robot_view, model_rows, interval=0.5):
        """Приймає моделі та параметри."""
        self.robot_model = robot_model
        self.robot_view = robot_view
        self.model_rows = model_rows
        self.interval = interval

        self.running = False
        self.thread = None

    def start(self):
        """Метод для запуску."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        """Метод для зупинки."""
        self.running = False

    def _run(self):
        """Цикл виконання."""
        while self.running:
            time.sleep(self.interval)
            Clock.schedule_once(lambda dt: self.update_robot_position())

    def update_robot_position(self):
        """Зміна позиції робота."""
        new_x = (self.robot_model.x * CellView.cell_size) - (CellView.cell_size // 1.5)
        new_y = (self.model_rows + 4 - self.robot_model.y) * CellView.cell_size

        self.robot_view.pos = (new_x, new_y)

        if self.robot_model.direction == Directions.UP:
            self.robot_view.robot_image.source = 'assets/robot_anim/robot_up.png'
        elif self.robot_model.direction == Directions.DOWN:
            self.robot_view.robot_image.source = 'assets/robot_anim/robot_down.png'
        elif self.robot_model.direction == Directions.LEFT:
            self.robot_view.robot_image.source = 'assets/robot_anim/robot_left.png'
        elif self.robot_model.direction == Directions.RIGHT:
            self.robot_view.robot_image.source = 'assets/robot_anim/robot_right.png'
