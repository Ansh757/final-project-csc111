"""
Final Project Title: ...

Objective: Create a visualization, that the users are able to see, that provides them
with the recommendations.

By: Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais

This file is Copyright (c) 2020 Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    """
    ...
    """

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        # Set columns
        self.rows = 4

        # Create a second gridlayout
        self.top_grid = GridLayout()
        # Set number of columns in our new top_grid
        self.top_grid.rows = 1

        # Add widgets
        self.add_widget(Label(text="Top Recommendations"))

        self.top_grid.add_widget(Button(text="Movie1"))
        self.top_grid.add_widget(Button(text="Movie 2 "))
        self.top_grid.add_widget(Button(text="Movie 3"))

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
