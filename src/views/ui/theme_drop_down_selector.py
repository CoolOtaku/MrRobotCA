from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

from src.views.ui.button_view import ButtonView


class ThemeDropDownSelector(BoxLayout):
    def __init__(self, theme_controller, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 25

        self.theme_controller = theme_controller
        self.main_button = ButtonView(text="Виберіть тему")
        self.dropdown = DropDown()

        for theme in self.theme_controller.themes.keys():
            btn = ButtonView(text=theme.capitalize(), size_hint_y=None, height=35)
            btn.bind(on_release=lambda btn: self.select_theme(btn.text.lower()))
            self.dropdown.add_widget(btn)

        self.main_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x.capitalize()))

        self.add_widget(self.main_button)

    def select_theme(self, theme_name):
        self.theme_controller.change_theme(theme_name)
        self.dropdown.select(theme_name)
        self.set_theme(self.theme_controller.themes[theme_name])

    def set_theme(self, theme):
        self.main_button.set_theme(theme)
        for btn in self.dropdown.container.children:
            btn.set_theme(theme)
