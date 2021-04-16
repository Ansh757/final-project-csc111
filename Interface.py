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
from extracting_reviews import trailers, get_images, fetch_movie_reviews
import graph_vertex
import main
import pprint

x = input("Enter")
movies = main.get_portion_file(x)


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

    def image_appear(self):

        self.ids.my_image3.source = get_images(movies[0])

        self.ids.my_image2.source = get_images(movies[1])

        self.ids.my_image1.source = get_images(movies[2])


class P(FloatLayout):
    def ytube(self):
        show_trailer()

    def text1(self):
        description()

    def review1(self):
        reviews_1()


class P2(FloatLayout):
    def ytube2(self):
        show_trailer2()

    def text2(self):
        description2()

    def review2(self):
        reviews_2()


class P3(FloatLayout):
    def ytube3(self):
        show_trailer3()

    def text3(self):
        description3()

    def review3(self):
        reviews_3()


class Top3(App):
    def build(self):
        Window.size = (700, 600)
        return MyGrid()


def show_popup():
    """
    ...
    """
    show = P()
    popup_window = Popup(title=movies[0], content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_popup2():
    """
    ...
    """
    show = P2()
    popup_window = Popup(title=movies[1], content=show, size_hint=(None, None), size=(550, 600))
    popup_window.open()


def show_popup3():
    """
    ...
    """
    show = P3()
    popup_window = Popup(title=movies[2], content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_trailer():
    trailers(movies[0])


def show_trailer2():
    trailers(movies[1])


def show_trailer3():
    trailers(movies[2])


def description():
    pprint.pprint("this is a story about....")


def description2():
    pprint.pprint("this is a story about....")


def description3():
    pprint.pprint("this is a story about....")


def reviews_1():
    pprint.pprint(fetch_movie_reviews(movies[0]))


def reviews_2():
    pprint.pprint(fetch_movie_reviews(movies[1]))


def reviews_3():
    pprint.pprint(fetch_movie_reviews(movies[2]))


if __name__ == '__main__':
    Top3().run()
