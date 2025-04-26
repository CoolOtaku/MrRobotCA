from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from src.controllers.automaton_controller import AutomatonController
from src.models.grid_model import GridModel
from src.models.robot_model import RobotModel
from src.views.grid_view import GridView
from src.views.cell_view import CellView


class CellularAutomatonApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None

    def build(self):
        grid_size = 30

        Window.size = (grid_size * CellView.cell_size, grid_size * CellView.cell_size ** 2)
        Window.resizable = False
        Window.title = 'Cellular Automaton'

        grid_model = GridModel(grid_size)
        grid_view = GridView(grid_model)
        robot_model = RobotModel(grid_size // 2, grid_size // 2)

        self.root = BoxLayout(orientation='vertical')
        self.root.add_widget(grid_view)

        step_button = Button(text="Крок", size_hint=(1, 0.1))
        step_button.bind(on_press=self.step)
        self.root.add_widget(step_button)

        self.controller = AutomatonController(grid_model, robot_model, grid_model.cell_views)

        return self.root

    def step(self, instance):
        self.controller.step()

if __name__ == "__main__":
    CellularAutomatonApp().run()
