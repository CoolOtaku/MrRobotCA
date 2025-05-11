import random

class StartupConditionController:
    def __init__(self, grid_model, robot_model, args):
        """Приймає моделі та параметри."""
        self.grid_model = grid_model
        self.robot_model = robot_model
        self.args = args

    def apply(self):
        """Визначає та активує початкові умови."""
        if "random_pos" in self.args:
            self.robot_model.x = random.randint(0, self.grid_model.cols - 1)
            self.robot_model.y = random.randint(0, self.grid_model.rows - 1)
            print(f"Позиція робота: ({self.robot_model.x}, {self.robot_model.y})")

        if "random_dir" in self.args:
            self.robot_model.direction = random.choice(list(type(self.robot_model.direction)))
            print(f"Напрямок робота: ({self.robot_model.direction})")

        if "cross" in self.args:
            center_x = self.grid_model.cols // 2
            center_y = self.grid_model.rows // 2
            for dx in range(-3, 4):
                self.grid_model.get_cell(center_x + dx, center_y)[1].toggle_state()
                self.grid_model.get_cell(center_x, center_y + dx)[1].toggle_state()

        if "random_active" in self.args:
            for model, view in self.grid_model.get_cells():
                model.is_active = random.choice([True, False])
                view.update_color(model.is_active)

        if "all_active" in self.args:
            for model, view in self.grid_model.get_cells():
                view.toggle_state()
