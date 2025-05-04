import os

from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

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
        self.grid_view.size_hint = (None, None)
        self.grid_view.size = (model.cols * CellView.cell_size, model.rows * CellView.cell_size)
        self.grid_view.pos_hint = {'top': 1}
        self.add_widget(self.grid_view)

        self.robot_view = RobotView()
        self.robot_view.pos = (0, 0)
        self.add_widget(self.robot_view)

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
