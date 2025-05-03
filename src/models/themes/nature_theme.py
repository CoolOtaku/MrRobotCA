from src.models.themes.theme_model import ThemeModel


class NatureTheme(ThemeModel):
    """Ініціалізує супер клас."""
    def __init__(self):
        super().__init__(background_window="assets/themes/nature/water.jpg",
                         background_button="assets/themes/nature/btn_bg.png",
                         background_cell_active="assets/themes/nature/stone.jpg",
                         background_cell_inactive="assets/themes/nature/grass.jpg")
