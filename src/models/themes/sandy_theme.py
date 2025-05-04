from src.models.themes.theme_model import ThemeModel


class SandyTheme(ThemeModel):
    def __init__(self):
        """Ініціалізує супер клас теми."""
        super().__init__(name="Піщана Тема",
                         background_window="assets/themes/sandy/sea.jpg",
                         background_button="assets/themes/sandy/btn_bg.png",
                         background_cell_active="assets/themes/sandy/stone.jpg",
                         background_cell_inactive="assets/themes/sandy/sand.jpg")
