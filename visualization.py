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
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # # Set columns
        # self.cols = 1
        #
        # # Create a second gridlayout
        # self.top_grid = GridLayout()
        # # Set number of columns in our new top_grid
        # self.top_grid.cols = 2
        #
        # # Add widgets
        # self.top_grid.add_widget(Label(text="Name: "))
        # # Add Input Box
        # self.name = TextInput(multiline=True)
        # self.top_grid.add_widget(self.name)
        #
        # self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # # Add Input Box
        # self.pizza = TextInput(multiline=False)
        # self.top_grid.add_widget(self.pizza)
        #
        # self.top_grid.add_widget(Label(text="Favorite Color: "))
        # # Add Input Box
        # self.color = TextInput(multiline=False)
        # self.top_grid.add_widget(self.color)
        #
        # # Add the new top_grid to our app
        # self.add_widget(self.top_grid)
        #


        self.cols = 1

        # Creating the top layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.movie1 = Button(text='Movie1', font_size=13)
        self.movie2 = Button(text='Movie1', font_size=13)
        self.movie3 = Button(text='Movie1', font_size=13)
        self.movie4 = Button(text='Movie1', font_size=13)
        self.movie5 = Button(text='Movie1', font_size=13)
        self.movie6 = Button(text='Movie1', font_size=13)
        self.movie7 = Button(text='Movie1', font_size=13)
        self.movie8 = Button(text='Movie1', font_size=13)
        self.movie9 = Button(text='Movie1', font_size=13)

        self.add_widget((Label(text='Top Recommendations: ')))
        self.top_grid.add_widget(self.movie1)
        self.top_grid.add_widget(self.movie2)
        self.top_grid.add_widget(self.movie3)
        self.top_grid.add_widget(self.movie4)
        self.add_widget(Label(text = "Other Recommendations"))
        self.top_grid.add_widget(self.movie5)
        self.top_grid.add_widget(self.movie6)
        self.top_grid.add_widget(self.movie7)
        self.top_grid.add_widget(self.movie8)
        self.top_grid.add_widget(self.movie9)

        self.add_widget(self.top_grid)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
