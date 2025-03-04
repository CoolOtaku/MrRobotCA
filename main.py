from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Cell(Button):
    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self.x_pos = x
        self.y_pos = y
        self.is_active = False  # False - пасивна, True - активна
        self.update_color()
        self.bind(on_press=self.toggle_state)

    def toggle_state(self, instance):
        """Перемикає стан клітинки при натисканні."""
        self.set_state(not self.is_active)

    def set_state(self, state):
        """Встановлює стан клітинки та оновлює її вигляд."""
        self.is_active = state
        self.update_color()

    def update_color(self):
        """Оновлює колір клітинки відповідно до її стану."""
        self.background_color = (0, 0, 0, 1) if self.is_active else (1, 1, 1, 1)


class CellularAutomatonApp(App):
    def build(self):
        self.grid_size = 10  # Розмір сітки
        layout = GridLayout(cols=self.grid_size, rows=self.grid_size)

        self.cells = {}  # Словник для доступу до клітинок за координатами
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                cell = Cell(x, y)
                self.cells[(x, y)] = cell
                layout.add_widget(cell)

        return layout


if __name__ == "__main__":
    CellularAutomatonApp().run()
