from kivy.app import App

from src.views.grid_view import GridView


class CellularAutomatonApp(App):
    def build(self):
        grid_size = 10
        return GridView(grid_size)


if __name__ == "__main__":
    CellularAutomatonApp().run()
