from kivy.uix.floatlayout import FloatLayout

from src.views.cell_view import CellView
from src.views.grid_view import GridView
from src.views.robot_view import RobotView


class FieldView(FloatLayout):
    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)

        self.grid_view = GridView(model)
        self.grid_view.size_hint = (None, None)
        self.grid_view.size = (model.cols * CellView.cell_size, model.rows * CellView.cell_size)
        self.grid_view.pos_hint = {'top': 1}
        self.add_widget(self.grid_view)

        """self.robot_view = RobotView(source='robot.png', width=50, height=50)
        self.robot_view.pos = (0, 0)  # початкова позиція
        self.add_widget(self.robot_view)"""

    def move_robot_to_cell(self, x, y, cell_width, cell_height):
        new_x = x * cell_width
        new_y = y * cell_height
        self.robot_view.pos = (new_x, new_y)
