from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class CellView(Widget):
    cell_size = 20

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

        """Задає розмір."""
        self.size_hint = (None, None)
        self.size = (20, 20)

        """Задає дефолтний колір."""
        with self.canvas:
            self.color = Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.update_color(self.model.is_active)

    def toggle_state(self):
        """Перемикає стан моделі та оновлює вигляд."""
        self.model.toggle()
        self.update_color(self.model.is_active)

    def update_color(self, is_active):
        """Оновлює колір клітинки відповідно до стану моделі."""
        self.color.rgba = (0, 0, 0, 1) if is_active else (1, 1, 1, 1)

    def update_graphics(self, *args):
        """Оновлює графіку В'юшки."""
        self.rect.pos = self.pos
        self.rect.size = self.size
