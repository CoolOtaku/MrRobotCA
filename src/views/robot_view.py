from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image


class RobotView(Widget):
    source = StringProperty('assets/robot_anim/robot_down.png')
    is_visible = BooleanProperty(True)

    def __init__(self, **kwargs):
        """Приймає параметри та ініціалізує супер клас."""
        super(RobotView, self).__init__(**kwargs)
        self.size_hint = (None, None)

        self.robot_image = Image(
            source=self.source,
            size_hint=self.size_hint,
            size=(50, 50),
            pos=self.pos
        )

        self.add_widget(self.robot_image)
        self.bind(pos=self.update_position, is_visible=self.update_visibility)

    def show(self):
        """Відображає."""
        self.is_visible = True

    def hide(self):
        """Ховає."""
        self.is_visible = False

    def update_position(self, *args):
        """Оновлює позицію відображення робота."""
        self.robot_image.pos = self.pos

    def update_visibility(self, *args):
        """Оновлює відображення робота."""
        self.robot_image.opacity = 1 if self.is_visible else 0
