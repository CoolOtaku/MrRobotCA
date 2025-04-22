from kivy.uix.gridlayout import GridLayout
from src.models.cell_model import CellModel
from src.views.cell_view import CellView


class GridView(GridLayout):
    def __init__(self, grid_size, **kwargs):
        super().__init__(**kwargs)
        self.cols = grid_size
        self.rows = grid_size
        self.cell_models = {}
        self.cell_views = {}

        for y in range(self.rows):
            for x in range(self.cols):
                model = CellModel(x, y)
                view = CellView(model)
                self.cell_models[(x, y)] = model
                self.cell_views[(x, y)] = view
                self.add_widget(view)
