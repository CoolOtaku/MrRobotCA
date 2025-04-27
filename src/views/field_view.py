from kivy.uix.floatlayout import FloatLayout

from src.views.robot_view import RobotView
from src.views.grid_view import GridView
from src.views.cell_view import CellView


class FieldView(FloatLayout):
    def __init__(self, model, **kwargs):
        """Приймає модель та ініціалізує супер клас."""
        super().__init__(**kwargs)

        self.grid_view = GridView(model)
        self.grid_view.size_hint = (None, None)
        self.grid_view.size = (model.cols * CellView.cell_size, model.rows * CellView.cell_size)
        self.grid_view.pos_hint = {'top': 1}
        self.add_widget(self.grid_view)

        self.robot_view = RobotView()
        self.robot_view.pos = (0, 0)
        self.add_widget(self.robot_view)
