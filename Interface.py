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

from extracting_reviews import trailers


class MyGrid(Widget):
    """
    ...
    """

    def btn(self):
        show_popup()

    def btn2(self):
        show_popup2()

    def btn3(self):
        show_popup3()


class P(FloatLayout):
    def ytube(self):
        show_trailer()


class P2(FloatLayout):
    def ytube2(self):
        show_trailer2()


class P3(FloatLayout):
    def ytube3(self):
        show_trailer3()


class MyApp(App):
    def build(self):
        Window.size = (700, 600)
        return MyGrid()


def show_popup():
    """
    ...
    """
    show = P()
    popup_window = Popup(title="Movie 1", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_popup2():
    """
    ...
    """
    show = P2()
    popup_window = Popup(title="Movie 2", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_popup3():
    """
    ...
    """
    show = P3()
    popup_window = Popup(title="Movie 3", content=show, size_hint=(None, None), size=(400, 500))

    popup_window.open()


def show_trailer():
    trailers('Wonder Woman')


def show_trailer2():
    trailers('Dark Tower')


def show_trailer3():
    trailers('Avatar')


if __name__ == '__main__':
    MyApp().run()
