class CellModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_active = False # False - пасивна, True - активна

    def toggle(self):
        self.is_active = not self.is_active

    def set_state(self, state: bool):
        self.is_active = state
