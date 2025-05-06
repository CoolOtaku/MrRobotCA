import threading
import time

from kivy.clock import Clock


class DebugController:
    def __init__(self, robot_model, interval=0.5):
        """Приймає модель та параметри."""
        self.robot_model = robot_model
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
        print(f"{self.robot_model.x},\n{self.robot_model.y}")
