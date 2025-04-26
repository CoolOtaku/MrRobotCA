class GridModel:
    def __init__(self, grid_size):
        self.cols = grid_size
        self.rows = grid_size
        self.cell_models = {}
        self.cell_views = {}

    def set_cell(self, x, y, cell_model, cell_view):
        self.cell_models[(x, y)] = cell_model
        self.cell_views[(x, y)] = cell_view

    def get_cell(self, x, y):
        return self.cell_models[(x, y)]
