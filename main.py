from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from src.controllers.automaton_controller import AutomatonController
from src.controllers.аuto_step_controller import AutoStepController
from src.models.robot_model import RobotModel
from src.models.grid_model import GridModel
from src.views.field_view import FieldView
from src.views.grid_view import GridView
from src.views.cell_view import CellView


class CellularAutomatonApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
        self.auto_step_controller = None

    def build(self):
        """Ініцілізація вікна та його конфігурація."""
        Window.size = (GridView.grid_size * CellView.cell_size, GridView.grid_size * CellView.cell_size ** 2)
        Window.clearcolor = (1, 0, 0, 1)
        Window.title = 'Cellular Automaton'
        Window.set_icon('robot.png')

        """Створення контейнера для таблиці та кнопок."""
        self.root = BoxLayout(orientation='vertical')

        """Створення та монтування поля."""
        grid_model = GridModel(GridView.grid_size)
        field_view = FieldView(grid_model)
        robot_model = RobotModel(GridView.grid_size // 2, GridView.grid_size // 2)
        self.root.add_widget(field_view)

        """Створення кнопок та встановлення в контейнер."""
        button_layout = BoxLayout(size_hint=(1, 0.1))
        step_button = Button(text="Крок")
        step_button.bind(on_press=self.step)
        auto_button = Button(text="Авто")
        auto_button.bind(on_press=self.toggle_auto)
        button_layout.add_widget(step_button)
        button_layout.add_widget(auto_button)
        self.root.add_widget(button_layout)

        """Ініцілізація контролерів."""
        self.controller = AutomatonController(grid_model, robot_model, grid_model.cell_views)
        self.auto_step_controller = AutoStepController(self.step)

        return self.root

    def step(self, *args):
        self.controller.step()

    def toggle_auto(self, *args):
        if self.auto_step_controller.running:
            self.auto_step_controller.stop()
        else:
            self.auto_step_controller.start()

if __name__ == "__main__":
    CellularAutomatonApp().run()
