from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class ToggleVisibilityButton(ButtonBehavior, Image):
    def __init__(self, robot_view, **kwargs):
        """Приймає в'юшку та ініціалізує супер клас."""
        super(ToggleVisibilityButton, self).__init__(**kwargs)
        self.robot_view = robot_view
        self.update_icon()

    def on_press(self):
        """При нажиманні виконує функції."""
        if self.robot_view.is_visible:
            self.robot_view.hide()
        else:
            self.robot_view.show()
        self.update_icon()

    def update_icon(self):
        """Оновляє іконку."""
        if self.robot_view.is_visible:
            self.source = 'assets/show.png'
        else:
            self.source = 'assets/hide.png'
