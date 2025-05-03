class GridModel:
    def __init__(self, grid_size):
        """Приймає параметри."""
        self.cols = grid_size
        self.rows = grid_size
        self.cell_models = {}
        self.cell_views = {}

    def set_cell(self, x, y, cell_model, cell_view):
        """Вставляє клітинку."""
        self.cell_models[(x, y)] = cell_model
        self.cell_views[(x, y)] = cell_view

    def get_cell(self, x, y):
        """Зчитує клітинку."""
        return self.cell_models[(x, y)], self.cell_views[(x, y)]

    def get_cells(self):
        res = []
        for y in range(self.rows):
            for x in range(self.cols):
                res.append(self.get_cell(x, y))

        return tuple(res)