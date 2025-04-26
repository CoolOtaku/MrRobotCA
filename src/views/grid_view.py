from kivy.uix.gridlayout import GridLayout

from src.models.cell_model import CellModel
from src.views.cell_view import CellView


class GridView(GridLayout):
    grid_size = 30

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.rows = model.rows
        self.cols = model.cols

        for y in range(self.rows):
            for x in range(self.cols):
                cell_model = CellModel(x, y)
                cell_view = CellView(cell_model)

                self.model.set_cell(x, y, cell_model, cell_view)
                self.add_widget(cell_view)
