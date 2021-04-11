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
from kivy.uix.popup import Popup


class MyGrid(Widget):
    """
    ...
    """

    def btn(self):
        show_popup()


class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        Window.size = (800, 900)
        return MyGrid()


def show_popup():
    """
    ...
    """
    show = P()
    popup_window = Popup(title="Movie Name", content=show, size_hint=(None, None), size=(800, 900))

    popup_window.open()


if __name__ == '__main__':
    MyApp().run()
