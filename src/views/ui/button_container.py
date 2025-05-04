from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout


class ButtonContainerView(BoxLayout):
    def __init__(self, **kwargs):
        """Приймає параметри та ініціалізує супер клас."""
        super().__init__(**kwargs)

        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 0)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        """Оновляє задній фон"""
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def set_theme(self, theme):
        """Ставить тему для віджета і його дочірніх віджетів."""
        self.canvas.before.clear()
        with self.canvas.before:
            if isinstance(theme.background_window, tuple):
                self.bg_color = Color(*theme.background_window)
                self.bg_rect = Rectangle(pos=self.pos, size=self.size)
            else:
                texture = CoreImage(theme.background_window).texture
                self.bg_rect = Rectangle(texture=texture, pos=self.pos, size=self.size)

        self._update_bg()

        for button in self.children:
            if hasattr(button, 'set_theme'):
                button.set_theme(theme)
