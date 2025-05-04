from src.models.themes.cyberpunk_theme import CyberpunkTheme
from src.models.themes.nature_theme import NatureTheme
from src.models.themes.sandy_theme import SandyTheme
from src.models.themes.theme_model import ThemeModel


class ThemeController:
    def __init__(self, window, button_container, field_view):
        """Приймає параметри."""
        self.window = window
        self.button_container = button_container
        self.field_view = field_view

        self.themes = {
            "symple_theme": ThemeModel(),
            "nature_theme": NatureTheme(),
            "cyberpunk_theme": CyberpunkTheme(),
            "sandy_theme": SandyTheme()
        }

        self.change_theme()

    def change_theme(self, theme_key="symple_theme"):
        """Метод для зміни теми."""
        if theme_key in self.themes:
            theme = self.themes[theme_key]
            if isinstance(theme.background_window, tuple):
                self.window.clearcolor = theme.background_window
                self.field_view.bg.source = 'assets/transparent.png'
            else:
                self.window.clearcolor = (1, 1, 1, 1)
                self.field_view.bg.source = theme.background_window

            self.field_view.set_theme(theme)
            self.button_container.set_theme(theme)

    def get_default_theme(self):
        """Повертає стандартну тему."""
        return self.themes["symple_theme"]
