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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

class MyGrid(Widget):
    """
    ...
    """
    pass


class MyApp(App):
    def build(self):
        Window.size = (800, 900)
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
