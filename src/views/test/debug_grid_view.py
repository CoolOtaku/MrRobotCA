from kivy.uix.gridlayout import GridLayout

from src.views.cell_view import CellView
from src.views.test.debug_cell_view import DebugCellView


class DebugGridView(GridLayout):
    def __init__(self, rows, cols, **kwargs):
        """Приймає параметри та ініціалізує супер клас."""
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = cols

        self.size_hint = (None, None)
        self.size = (self.cols * CellView.cell_size, self.rows * CellView.cell_size)
        self.pos_hint = {'top': 1}

        for y in range(self.rows):
            for x in range(self.cols):
                debug_cell = DebugCellView(x, y)
                self.add_widget(debug_cell)
