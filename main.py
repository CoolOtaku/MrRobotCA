from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from src.controllers.test.debug_controller import DebugController
from src.views.ui.toggle_visibility_button import ToggleVisibilityButton
from src.views.ui.theme_drop_down_selector import ThemeDropDownSelector
from src.controllers.robot_view_controller import RobotViewController
from src.controllers.automaton_controller import AutomatonController
from src.controllers.аuto_step_controller import AutoStepController
from src.views.ui.button_container import ButtonContainerView
from src.controllers.theme_controller import ThemeController
from src.views.ui.button_view import ButtonView
from src.models.robot_model import RobotModel
from src.models.grid_model import GridModel
from src.views.field_view import FieldView
from src.views.grid_view import GridView
from src.views.cell_view import CellView


class CellularAutomatonApp(App):
    is_debug_mode = True

    def __init__(self, **kwargs):
        """Ініціалізація контролерів та супер класу."""
        super().__init__(**kwargs)
        self.automaton_controller = None
        self.auto_step_controller = None
        self.robot_view_controller = None
        self.theme_controller = None

    def build(self):
        """Ініцілізація вікна та його конфігурація."""
        Window.size = (GridView.grid_size * CellView.cell_size, GridView.grid_size * CellView.cell_size ** 2)
        Window.title = 'Cellular Automaton'
        Window.set_icon('assets/icon.png')

        # Створення контейнера для поля та кнопок.
        self.root = BoxLayout(orientation='vertical')

        # Створення та монтування поля.
        grid_model = GridModel(GridView.grid_size)
        field_view = FieldView(grid_model)
        robot_model = RobotModel(GridView.grid_size // 2, GridView.grid_size // 2)
        self.root.add_widget(field_view)

        # Створення кнопок та встановлення в контейнер.
        button_container = ButtonContainerView(size_hint=(1, 0.1))
        step_button = ButtonView(text="Крок")
        step_button.bind(on_press=self.step)

        auto_button = ButtonView(text="Авто")
        auto_button.bind(on_press=self.toggle_auto)

        visible_button = ToggleVisibilityButton(field_view.robot_view)

        # Додавання кнопок до контейнера.
        button_container.add_widget(step_button)
        button_container.add_widget(auto_button)
        button_container.add_widget(visible_button)
        self.root.add_widget(button_container)

        # Створення та запуск контролерів.
        self.automaton_controller = AutomatonController(grid_model, robot_model)
        self.auto_step_controller = AutoStepController(self.step)
        self.robot_view_controller = RobotViewController(robot_model, field_view.robot_view, grid_model.rows)
        self.theme_controller = ThemeController(Window, button_container, field_view)
        self.robot_view_controller.start()

        # Якщо увімкнений режим налагодження.
        if self.is_debug_mode:
            debug_controller = DebugController(robot_model)
            debug_controller.start()

        # Створення та додавання до контейнера віджета з темами.
        theme_selector = ThemeDropDownSelector(self.theme_controller)
        theme_selector.set_theme(self.theme_controller.get_default_theme())
        self.root.add_widget(theme_selector)

        # Повернення готового вікна.
        return self.root

    def step(self, *args):
        """Запуск одного ходу."""
        self.automaton_controller.step()

    def toggle_auto(self, *args):
        """Запуск циклу ходів."""
        if self.auto_step_controller.running:
            self.auto_step_controller.stop()
        else:
            self.auto_step_controller.start()

if __name__ == "__main__":
    CellularAutomatonApp().run()
