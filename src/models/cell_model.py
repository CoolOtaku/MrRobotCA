class CellModel:
    def __init__(self, x, y):
        """Приймає параметри."""
        self.x = x
        self.y = y
        self.is_active = False

    def toggle(self):
        """Метод на тригер зміни статусу."""
        self.is_active = not self.is_active

    def set_state(self, state: bool):
        """Метод для зміни статусу клітинки."""
        self.is_active = state
