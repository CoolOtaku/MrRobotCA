from kivy.uix.label import Label
from kivy.uix.widget import Widget

from src.views.cell_view import CellView


class DebugCellView(Widget):
    def __init__(self, x, y, **kwargs):
        """Приймає параметри та ініціалізує супер клас."""
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (CellView.cell_size, CellView.cell_size)

        self.label = Label(text=f"{x},\n{y}",
                           size=self.size,
                           size_hint=(None, None),
                           font_size=8,
                           color=(1, 0, 0, 1))

        self.add_widget(self.label)
        self.bind(pos=self.update_position)

    def update_position(self, *args):
        """Оновлює позицію."""
        self.label.pos = self.pos
