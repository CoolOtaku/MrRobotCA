from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

from src.views.ui.button_view import ButtonView


class ThemeDropDownSelector(BoxLayout):
    def __init__(self, theme_controller, **kwargs):
        """Приймає контролер тем та ініціалізує супер клас."""
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 25

        self.theme_controller = theme_controller
        self.main_button = ButtonView(text="Виберіть Тему")
        self.dropdown = DropDown()

        self.key_to_button_text = {}
        self.button_text_to_key = {}

        for key, theme in self.theme_controller.themes.items():
            button_text = getattr(theme, 'name', key.capitalize())
            self.key_to_button_text[key] = button_text
            self.button_text_to_key[button_text] = key

            btn = ButtonView(text=button_text, size_hint_y=None, height=35)
            btn.bind(on_release=lambda btn, bt=button_text: self.select_theme_by_text(bt))
            self.dropdown.add_widget(btn)

        self.main_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x))

        self.add_widget(self.main_button)

    def select_theme_by_text(self, button_text):
        """Вибирає тему визначаючи його по назві теми."""
        theme_key = self.button_text_to_key[button_text]
        self.theme_controller.change_theme(theme_key)
        self.dropdown.select(button_text)
        self.set_theme(self.theme_controller.themes[theme_key])

    def set_theme(self, theme):
        """Ставить тему для віджета і його дочірніх віджетів."""
        self.main_button.set_theme(theme)
        for btn in self.dropdown.container.children:
            btn.set_theme(theme)
