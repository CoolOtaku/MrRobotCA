from src.models.themes.theme_model import ThemeModel


class CyberpunkTheme(ThemeModel):
    def __init__(self):
        """Ініціалізує супер клас теми."""
        super().__init__(name="Кіберпанк Тема",
                         background_window="assets/themes/cyberpunk/circuit_board.jpg",
                         background_button="assets/themes/cyberpunk/btn_bg.png",
                         background_cell_active="assets/themes/cyberpunk/motherboard.jpg",
                         background_cell_inactive="assets/themes/cyberpunk/blue_grey_carpet.jpg")
