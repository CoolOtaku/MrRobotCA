from src.models.themes.theme_model import ThemeModel


class NatureTheme(ThemeModel):
    def __init__(self):
        """Ініціалізує супер клас теми."""
        super().__init__(name="Природня Тема",
                         background_window="assets/themes/nature/water.jpg",
                         background_button="assets/themes/nature/btn_bg.png",
                         background_cell_active="assets/themes/nature/soil.jpg",
                         background_cell_inactive="assets/themes/nature/grass.jpg")
