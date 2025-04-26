from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty


class RobotView(Widget):
    source = StringProperty('robot.png')
    size_hint_x = NumericProperty(None)
    size_hint_y = NumericProperty(None)
    width = NumericProperty(50)
    height = NumericProperty(50)

    def __init__(self, **kwargs):
        super(RobotView, self).__init__(**kwargs)

        self.robot_image = Image(
            source=self.source,
            size_hint=(None, None),
            size=(self.width, self.height),
            pos=self.pos
        )
        self.add_widget(self.robot_image)

        self.bind(pos=self.update_position)
        self.bind(size=self.update_size)

    def update_position(self, *args):
        self.robot_image.pos = self.pos

    def update_size(self, *args):
        self.robot_image.size = (self.width, self.height)
