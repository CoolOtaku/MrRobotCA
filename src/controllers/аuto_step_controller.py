from kivy.clock import Clock

import threading
import time


class AutoStepController:
    def __init__(self, step_function, interval=0.5):
        self.step_function = step_function
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            time.sleep(self.interval)
            Clock.schedule_once(lambda dt: self.step_function())
