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
from extracting_reviews import trailers, get_images
import graph_vertex
import main
#
#
# def _load_graph(portion_file):
#     return main.load_graph(portion_file)
#
#
# def user_prompts(portion_file: str) -> str:
#     """
#     Creates a prompt for the user to pick a preferred movie based on filtered information
#
#     Precondition:
#         - input movie must be in imdb dataset
#     """
#     # g = filtered_graph('portions/portion1.csv', genre=genre, year=year, director=director,
#     #                    language=language, country=country)
#     g = _load_graph(portion_file)
#
#     for _ in range(len(g.get_all_vertices())):
#         movie_title = input("What is a movie you like?")
#         if movie_title in g.get_all_vertices():
#             return movie_title
#         print("Invalid selection. Please choose another movie")
#
#
# def get_portion_file(file: str) -> list[str]:
#     """..."""
#     new_graph = _load_graph(file)
#     get_movies = new_graph.movie_recs(main.user_prompts(file))
#     return get_movies

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
        self.ids.my_image1.source = get_images(movies[0])

        self.ids.my_image2.source = get_images(movies[1])

        self.ids.my_image3.source = get_images(movies[2])

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
    popup_window = Popup(title="Movie 3", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_trailer():
    trailers('Wonder Woman')


def show_trailer2():
    trailers('Dark Tower')


def show_trailer3():
    trailers('Avatar')


def description():
    print("this is a story about....")


def description2():
    print("this is a story about....")


def description3():
    print("this is a story about....")


def reviews_1():
    print("Reviews for movie 1")


def reviews_2():
    print("Reviews for movie 2")


def reviews_3():
    print("Reviews for movie 3")


def show_image():
    return "'http://mysite.com/test.png'"


if __name__ == '__main__':
    Top3().run()
