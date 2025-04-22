from kivy.uix.button import Button


class CellView(Button):
    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.update_color()
        self.bind(on_press=self.toggle_state)

    def toggle_state(self, instance):
        """Перемикає стан моделі при натисканні та оновлює вигляд."""
        self.model.toggle()
        self.update_color()

    def update_color(self):
        """Оновлює колір клітинки відповідно до стану моделі."""
        self.background_color = (0, 0, 0, 1) if self.model.is_active else (1, 1, 1, 1)
