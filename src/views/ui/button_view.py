from kivy.uix.button import Button


class ButtonView(Button):
    def __init__(self, text, **kwargs):
        super().__init__(text=text, **kwargs)

    def set_theme(self, theme):
        if isinstance(theme.background_button, tuple):
            self.background_color = theme.background_button
            self.background_normal = 'assets/transparent.png'
        else:
            self.background_color = (1, 1, 1, 1)
            self.background_normal = theme.background_button
