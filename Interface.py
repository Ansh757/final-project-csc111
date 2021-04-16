from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
from extracting_reviews import trailers, get_images, fetch_movie_reviews

import main
import pprint

portions = input("Enter Portion File: ")
movies = main.loading_graph(portions)


class MyGrid(Widget):
    """
    ...
    """

    def button(self) -> None:
        """
        Represents the first button for Movie1 contains the popup once movie1 button is pressed
        """
        show_popup()

    def button2(self) -> None:
        """
        Represents the first button for Movie2 contains the popup once movie1 button is pressed
        """
        show_popup2()

    def button3(self) -> None:
        """
        Represents the first button for Movie3 contains the popup once movie1 button is pressed

        """
        show_popup3()

    def image_appear(self) -> None:
        """
        Once the "Top Recommendations" Button is pressed, it changes the images for movie1,
        movie2 and movie3 to their respective movie poster

        """
        self.ids.my_image3.source = get_images(movies[0])

        self.ids.my_image2.source = get_images(movies[1])

        self.ids.my_image1.source = get_images(movies[2])


class P(FloatLayout):
    """
    Class represents all of the items functions within popout for movie1, which is
    displayed once movie1 button is pressed
    """

    def ytube(self) -> None:
        """
        Function launches the show_trailer function, which refers to the "Click to See Trailer"
        button. Once clicked the button launches Youtube Trailer for movie1
        """
        show_trailer()

    def text1(self) -> None:
        """
        Function launches the description function which shows the description of movie1, only
        when the "Click for Description" button is clicked
        """
        description()

    def review1(self) -> None:
        """
        Function launches the reviews_1 function, which displays the reviews for movie1, once
        "Click for Reviews" is pressed.

        """
        reviews_1()


class P2(FloatLayout):
    """
    Class represents all of the items functions within popout for movie2, which is
    displayed once movie1 button is pressed
    """

    def ytube2(self) -> None:
        """
        Function launches the show_trailer2 function, which refers to the "Click to See Trailer"
        button. Once clicked the button launches Youtube Trailer for movie2
        """
        show_trailer2()

    def text2(self) -> None:
        """
        Function launches the description2 function which shows the description of movie2, only
        when the "Click for Description" button is clicked
        """
        description2()

    def review2(self) -> None:
        """
        Function launches the reviews_2 function, which displays the reviews for movie2, once
        "Click for Reviews" is pressed.
        """
        reviews_2()


class P3(FloatLayout):
    """
    Class represents all of the items functions within popout for movie3, which is
    displayed once movie1 button is pressed
    """

    def ytube3(self) -> None:
        """
        Function launches the show_trailer2 function, which refers to the "Click to See Trailer"
        button. Once clicked the button launches Youtube Trailer for movie3
        """
        show_trailer3()

    def text3(self) -> None:
        """
        Function launches the description3 function which shows the description of movie3, only
        when the "Click for Description" button is clicked
        """
        description3()

    def review3(self) -> None:
        """
        Function launches the reviews_3 function, which displays the reviews for movie3, once
        "Click for Reviews" is pressed.
        """
        reviews_3()


class Top3(App):
    """
    Class that inherits from App, and allows us to build the app
    """
    def build(self):
        """
        Function that builds the the Top3 App and returns MyGrid, which contains
        all of the properties for our GUI
        """
        Window.size = (700, 600)
        return MyGrid()


def show_popup() -> None:
    """
    Includes the properties for the pop up window once movie1 is clicked
    """
    visual1 = P()
    popup_movie1 = Popup(title=movies[0], content=visual1, size_hint=(None, None), size=(550, 600),
                         background_color='#696969')

    popup_movie1.open()


def show_popup2():
    """
    Includes the properties for the pop up window once movie2 is clicked
    """
    visual2 = P2()
    popup_movie2 = Popup(title=movies[1], content=visual2, size_hint=(None, None), size=(550, 600),
                         background_color='#696969')
    popup_movie2.open()


def show_popup3():
    """
    Includes the properties for the pop up window once movie3 is clicked
    """
    visual3 = P3()
    popup_movie3 = Popup(title=movies[2], content=visual3, size_hint=(None, None), size=(550, 600),
                         background_color='#696969')

    popup_movie3.open()


def show_trailer() -> None:
    """
    The function responsible for opening the Trailer once "Click for the Trailer" is pressed
    within the popup for movie1
    """
    trailers(movies[0])


def show_trailer2() -> None:
    """
    The function responsible for opening the Trailer once "Click for the Trailer" is pressed
    within the popup for movie2
    """

    trailers(movies[1])


def show_trailer3():
    """
    The function responsible for opening the Trailer once "Click for the Trailer" is pressed
    within the popup for movie1
    """
    trailers(movies[2])


def description():
    """
    Shows the description for movie1 once, "Click for the Description" is clicked within the
    popup for movie1
    """
    g = main.loading_graph(portions)
    info = g.movie_info(portions, [movies[0]])
    print(info.get(movies[0])[5])


def description2() -> None:
    """Shows the description for movie1 once, "Click for the Description" is clicked within the
    popup for movie2"""
    g = main.loading_graph(portions)
    info = g.movie_info(portions, [movies[1]])
    print(info.get(movies[1])[5])


def description3() -> None:
    """Shows the description for movie1 once, "Click for the Description" is clicked within the
    popup for movie3"""
    g = main.loading_graph(portions)
    info = g.movie_info(portions, [movies[2]])
    print(info.get(movies[2])[5])


def reviews_1() -> None:
    """
    Shows the top 4 reviews for movie1 once, "Click for the Reviews" is clicked within the
    popup for movie1
    """
    all_reviews = fetch_movie_reviews(movies[0])
    for i in range(0, 4):
        pprint.pprint(all_reviews.get("Review Description")[i])
        print(end='\n')


def reviews_2() -> None:
    """
    Shows the top 4 reviews for movie1 once, "Click for the Reviews" is clicked within the
    popup for movie2
    """
    all_reviews = fetch_movie_reviews(movies[1])
    for i in range(0, 4):
        pprint.pprint(all_reviews.get("Review Description")[i])
        print(end='\n')


def reviews_3() -> None:
    """
    Shows the top 4 reviews for movie1 once, "Click for the Reviews" is clicked within the
    popup for movie3
    """
    all_reviews = fetch_movie_reviews(movies[1])
    for i in range(0, 4):
        pprint.pprint(all_reviews.get("Review Description")[i])
        print(end='\n')


if __name__ == '__main__':
    Top3().run()
