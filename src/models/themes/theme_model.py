class ThemeModel:
    def __init__(self, background_window=(1, 0, 0, 1), background_button=(1, 0, 0, 1),
                 background_cell_active=(0, 0, 0, 1), background_cell_inactive=(1, 1, 1, 1)):
        """Приймає параметри та ініціалізує супер клас."""
        self.background_window = background_window
        self.background_button = background_button
        self.background_cell_active = background_cell_active
        self.background_cell_inactive = background_cell_inactive
