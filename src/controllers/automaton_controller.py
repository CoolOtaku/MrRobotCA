class AutomatonController:
    def __init__(self, grid_model, robot_model):
        """Приймає моделі."""
        self.grid_model = grid_model
        self.robot_model = robot_model

    def step(self):
        """Метод одного ходу описаного алгоритму."""
        x, y = self.robot_model.x, self.robot_model.y
        cell = self.grid_model.get_cell(x, y)

        if cell.is_active:
            cell.is_active = False
            self.robot_model.turn_left()
        else:
            cell.is_active = True
            self.robot_model.turn_right()

        self.grid_model.cell_views[(x, y)].update_color(cell.is_active)
        self.robot_model.move_forward()
