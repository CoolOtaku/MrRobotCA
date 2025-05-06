import os

from kivy.core.image import Image as CoreImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.app import App

from src.views.test.debug_grid_view import DebugGridView
from src.views.robot_view import RobotView
from src.views.grid_view import GridView
from src.views.cell_view import CellView


class FieldView(FloatLayout):
    def __init__(self, model, **kwargs):
        """Приймає модель та ініціалізує супер клас."""
        super().__init__(**kwargs)
        self.bg = Image(source='assets/transparent.png',
                        allow_stretch=True,
                        keep_ratio=False,
                        size_hint=(1, 1),
                        pos_hint={'x': 0, 'y': 0}
                        )
        self.add_widget(self.bg)

        self.grid_view = GridView(model)
        self.add_widget(self.grid_view)

        self.robot_view = RobotView()
        self.add_widget(self.robot_view)

        if App.get_running_app().is_debug_mode:
            self.debug_grid = DebugGridView(model.rows, model.cols)
            self.debug_grid.size = self.grid_view.size
            self.debug_grid.pos = self.grid_view.pos
            self.add_widget(self.debug_grid)

    def set_theme(self, theme):
        """Ставить тему для віджета і його дочірніх віджетів."""
        if not isinstance(theme.background_cell_active, tuple) and os.path.exists(theme.background_cell_active):
            CellView.active_bg = CoreImage(theme.background_cell_active).texture
            CellView.inactive_bg = CoreImage(theme.background_cell_inactive).texture
        else:
            CellView.active_bg = theme.background_cell_active
            CellView.inactive_bg = theme.background_cell_inactive

        for cellModel, cellView in self.grid_view.model.get_cells():
            cellView.update_color(cellModel.is_active)
