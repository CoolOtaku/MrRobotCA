from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class CellView(Widget):
    cell_size = 20
    active_bg = (0, 0, 0, 1)
    inactive_bg = (1, 1, 1, 1)

    def __init__(self, model, **kwargs):
        """Приймає модель та ініціалізує супер клас."""
        super().__init__(**kwargs)
        self.model = model

        self.size_hint = (None, None)
        self.size = (self.cell_size, self.cell_size)

        with self.canvas:
            self.color = Color(rgba=self.inactive_bg)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.update_color(self.model.is_active)

    def toggle_state(self):
        """Перемикає стан моделі та оновлює вигляд."""
        self.model.toggle()
        self.update_color(self.model.is_active)

    def update_color(self, is_active):
        """Оновлює колір клітинки відповідно до стану моделі."""
        if isinstance(self.active_bg, tuple):
            self.color.rgba = self.active_bg if is_active else self.inactive_bg
            self.rect.texture = None
        else:
            self.color.rgba = (1, 1, 1, 1)
            self.rect.texture = self.active_bg if is_active else self.inactive_bg

    def update_graphics(self, *args):
        """Оновлює графіку В'юшки."""
        self.rect.pos = self.pos
        self.rect.size = self.size
